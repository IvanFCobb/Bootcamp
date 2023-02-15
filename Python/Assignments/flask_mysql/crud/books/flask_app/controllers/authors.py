from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route('/authors')
def authors():
    authors = Author.get_all()
    return render_template('authors.html', all_authors=authors)


@app.route('/new')
def new():
    books = Book.get_all()
    return render_template('new_author.html', all_books=books)


@app.route('/create_author', methods=["POST"])
def create_author():
    data = {
        "book_id": request.form["book_id"],
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
    }
    Author.create_author(data)
    return redirect('/books/{}'.format(data["book_id"]))


@app.route('/authors/edit/<int:num>', methods=["POST", "GET"])
def edit_author_page(num):
    books = Book.get_all()
    author = author.get_one(num)
    return render_template('edit_author.html', author=author, all_books=books)


@app.route('/update_author/<int:num>', methods=["POST"])
def update_author(num):
    print("before update")
    data = {
        "book_id": request.form["book_id"],
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
    }
    Author.edit_author(data, num)
    print("after update")
    return redirect('/books/{}'.format(data["book_id"]))


@app.route('/authors/delete/<int:num>', methods=["POST", "GET"])
def delete_author(num):
    author = author.get_one(num)
    print(author.books_id)
    author.delete_author(num)
    return redirect('/books/{}'.format(author.books_id))
