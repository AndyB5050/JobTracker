from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class companies(db.Model):
    idCompanies = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(45), nullable=True)
    Description = db.Column(db.String(255), nullable=True)
    Link = db.Column(db.String(255), nullable=True)
    
class jobs(db.Model):
    idJobs = db.Column(db.Integer, primary_key=True)
    Role = db.Column(db.String(45), nullable=False)
    Description = db.Column(db.String(255), nullable=True)
    Link = db.Column(db.String(255), nullable=True)
    idCompanies = db.Column(db.Integer, db.ForeignKey('companies.idCompanies'), nullable=False)
    ApplicationStatus = db.Column(db.String(45), nullable=True)
    ApplicationDate = db.Column(db.Date, nullable=True)
    Notes = db.Column(db.String(255), nullable=True)
    

