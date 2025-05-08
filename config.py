import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:SallyLinus$7@localhost/jobtracker"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    