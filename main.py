import pandas as pd
import os

FILE_NAME = "job_data.csv"

# Create the file if it doesn't exist
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Company", "Role", "Link", "DateApplied", "Status", "Notes"])
    df.to_csv(FILE_NAME, index=False)

def add_job():
    company = input("Company name: ")
    role = input("Job title: ")
    link = input("Application link: ")
    date = input("Date applied (YYYY-MM-DD): ")
    status = input("Status (applied/interview/etc): ")
    notes = input("Notes: ")

    job = pd.DataFrame([[company, role, link, date, status, notes]],
                       columns=["Company", "Role", "Link", "DateApplied", "Status", "Notes"])
    job.to_csv(FILE_NAME, mode='a', header=False, index=False)
    print("✅ Job saved!\n")

def edit_jobs():
    df = pd.read_csv(FILE_NAME)
    print("\nYour Job Applications:\n")
    print(df)

    try:
        index = int(input("Enter the index of the job you want to edit: "))
        if index < 0 or index >= len(df):
            raise ValueError("Index out of range.")
    except ValueError as e:
        print(f"❌ Invalid input: {e}")
        return

    column = input("Enter the column name to edit (Company, Role, Link, DateApplied, Status, Notes): ")
    if column not in df.columns:
        print("❌ Invalid column name.")
        return

    new_value = input(f"Enter new value for {column}: ")
    df.at[index, column] = new_value
    df.to_csv(FILE_NAME, index=False)
    print("✅ Job updated!\n")

def view_jobs():
    df = pd.read_csv(FILE_NAME)
    pd.set_option('display.max_columns', None) 
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.width', 1000)
    print("\nYour Job Applications:\n")
    print(df)

def main():
    while True:
        print("\nJob Tracker Menu:")
        print("1. Add job")
        print("2. Edit job")
        print("3. View jobs")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_job()
        elif choice == "2":
            edit_jobs()
        elif choice == "3":
            view_jobs()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
