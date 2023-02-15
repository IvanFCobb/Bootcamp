from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.book import Book
from flask_app.models.author import Author


@app.route('/books')
def books():
    books = Book.get_all()
    print(books)
    return render_template('books.html', all_books=books)


@app.route('/create_book', methods=["POST"])
def create_book():
    data = {
        "title": request.form["title"],
    }
    Book.create_book(data)
    return redirect('/books')


@app.route('/books/<int:num>', methods=["POST", "GET"])
def show_book(num):
    print("test")
    book = book.get_one(num)
    authors = Author.get_authors_in_book(num)
    return render_template('show_book.html', book=book, all_authors=authors)
