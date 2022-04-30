from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# db = sqlite3.connect("book_collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-book-collection.db'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Book(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'
    
# db.create_all()

# book1 = Book(id=1, title='Harry Potter and the Sorcering Wizardry Stones', author='Conservative Heroine, J.K. Rowling', rating=9.5)

# db.session.add(book1)
# db.session.commit()

all_books = []


@app.route('/')
def home():

    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # dict = {}
        # dict['title'] = request.form['title']
        # dict['author'] = request.form['author']
        # dict['rating'] = request.form['rating']
        # all_books.append(dict)
        
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)
        
        print(all_books)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

