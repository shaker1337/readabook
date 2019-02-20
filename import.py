from flask import Flask, render_template, request
from models import *
import csv
import os

app = Flask(__name__)
db.init_app(app)


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



def main():
    SQLAlchemy.create_all(db)
    f = open("bookse.csv")
    csv_f = csv.reader(f)
    counter = 0
    for isbn, title, author, year in csv_f:
        b = Book(isbn=isbn, title=title, author=author, year=year)
        db.session.add(b)
        print(b.year)
        counter +=1
        if counter == 100:
            db.session.commit()
            counter=0
    print("done")
if __name__ == "__main__":
    with app.app_context():
        main()
