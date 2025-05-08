from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, companies, jobs

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def home():
    
    # Get filter and sort parameters from the request
    filter_company = request.args.get("filter_company", "")
    sort_by = request.args.get("sort_by", "ApplicationDate")  # Default sort by ApplicationDate
    sort_order = request.args.get("sort_order", "asc")  # Default sort order is ascending

    # Base query
    query = db.session.query(jobs, companies).join(companies)

    # Apply filtering
    if filter_company:
        query = query.filter(companies.Name.ilike(f"%{filter_company}%"))

    # Apply sorting
    if hasattr(jobs, sort_by):  # Check if the column exists in the jobs table
        sort_column = getattr(jobs, sort_by)
    elif hasattr(companies, sort_by):  # Check if the column exists in the companies table
        sort_column = getattr(companies, sort_by)
    else:
        sort_column = jobs.ApplicationDate  # Default column if sort_by is invalid

    # Sort ascending or descending based on the sort_order parameter
    if sort_order == "asc":
        query = query.order_by(sort_column.asc())
    else:
        query = query.order_by(sort_column.desc())

    # Execute the query
    joblist = query.all()
    

    return render_template("index.html", joblist=joblist, filter_company=filter_company, sort_by=sort_by, sort_order=sort_order)

@app.route("/add", methods=["GET", "POST"])
def add_job():

    # Check if the request method is POST (form submission)
    # If it is, retrieve the form data and create a new job entry
    # If the request method is GET, render the form template
    if request.method == "POST":
        CompanyName = request.form["CompanyName"]
        CompanyDescription = request.form["CompanyDescription"]
        CompanyLink = request.form["CompanyLink"]
        JobRole = request.form["JobRole"]
        JobDescription = request.form["JobDescription"]
        JobLink = request.form["JobLink"]
        ApplicationDate = request.form["ApplicationDate"]
        ApplicationStatus = request.form["ApplicationStatus"]
        ApplicationNotes = request.form["ApplicationNotes"]

        # Create a the new company to add to the database
        new_company = companies(Name=CompanyName, Description=CompanyDescription, Link=CompanyLink)
        # Add the new company to the session       
        db.session.add(new_company)
        # Commit the session to save the new company to the database
        db.session.commit()
       
        # Create a new job entry with the form data
        # The new job entry is linked to the new company by using the company's ID
        new_job = jobs(
           Role=JobRole, 
           Description=JobDescription, 
           Link=JobLink, 
           ApplicationDate=ApplicationDate, 
           ApplicationStatus=ApplicationStatus, 
           Notes=ApplicationNotes,
           idCompanies=new_company.idCompanies
           )
    
        # Add the new job to the session
        db.session.add(new_job)
        # Commit the session to save the new job to the database
         # Commit the session to save the new job to the database
         # Note: The company ID is automatically assigned when the company is added to the session and committed.
         # So, you can directly use new_company.idCompanies for the foreign key in jobs.         
        db.session.commit()
        

        return redirect("/")
    return render_template("add_job.html")


@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_job(index):

    # Pull the job entry from the database using the index
    job = db.session.query(jobs, companies).join(companies, jobs.idCompanies == companies.idCompanies).filter(jobs.idJobs == index).first()
    
    if not job:
        # job was not found so alert to the console and return a 404 error
        print("Job not found")
        return "Job not found", 404

    job_data, company_data = job

    if request.method == "GET":
        return render_template("edit_job.html", job=job_data, company=company_data)


    if request.method == "POST":
        # Update the job entry with the new values from the form

        # Pull the values from the form
        CompanyName = request.form["CompanyName"]
        CompanyDescription = request.form["CompanyDescription"]
        CompanyLink = request.form["CompanyLink"]
        JobRole = request.form["JobRole"]
        JobLink = request.form["JobLink"]
        ApplicationDate = request.form["ApplicationDate"]
        ApplicationStatus = request.form["ApplicationStatus"]
        ApplicationNotes = request.form["ApplicationNotes"]

        # Update the company data
        company_data.Name = CompanyName
        company_data.Description = CompanyDescription
        company_data.Link = CompanyLink

        # Update the job data
        job_data.Role = JobRole
        job_data.Link = JobLink
        job_data.ApplicationDate = ApplicationDate
        job_data.ApplicationStatus = ApplicationStatus
        job_data.Notes = ApplicationNotes

        # Commit the changes to the database
        try:
            db.session.commit()
            print("Job and company updated successfully")
        except Exception as e:
            db.session.rollback()
            print(f"Error updating job and company: {e}")
            return "Error updating job and company", 500
        
        return redirect("/")
        
    
    
    

if __name__ == "__main__":
    app.run(debug=True)