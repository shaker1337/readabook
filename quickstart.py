from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ririxxufiteerd:01290b42d7aebc8c4310a2cbcc7a5f88246448db28ed99b4074938a8f7bac1a3@ec2-54-247-125-116.eu-west-1.compute.amazonaws.com:5432/dbqtbt3j7tit0a'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
