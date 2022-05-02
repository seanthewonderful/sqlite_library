from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import all_

app = Flask(__name__)

# allbooks = [{'title': 'Natalie', 'author': 'Sean', 'rating': '5'}, {'title': 'Sean', 'author': 'Natalie', 'rating': '4'}]


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-book-collection.db'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    
db.create_all()

data = Book.query.all()
book = db.session.query(Book).filter(Book.title=='Potter').first()
# print(data[0].title)
print(book)