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
        "num_of_pages": request.form["num_of_pages"],
    }
    Book.save(data)
    return redirect('/books')


@app.route('/books/<int:id>', methods=["POST", "GET"])
def show_book(id):
    data = {
        "id": id
    }
    return render_template('show_book.html', book=Book.get_by_id(data), unfavorited_authors=Author.unfavorited_authors(data))


@app.route('/join/author', methods=["POST", "GET"])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/books/{request.form['book_id']}")
