from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route('/', methods=["GET"])
def index():
    return redirect('/authors')


@app.route('/authors')
def authors():
    authors = Author.get_all()
    return render_template('authors.html', all_authors=authors)


@app.route('/create_author', methods=["POST"])
def create_author():
    data = {
        "name": request.form["name"],
    }
    Author.save(data)
    return redirect('/authors')


@app.route('/authors/<int:id>', methods=["POST", "GET"])
def show_author(id):
    data = {
        "id": id
    }
    return render_template('show_author.html', author=Author.get_by_id(data), unfavorited_books=Book.unfavorited_books(data))


@app.route('/join/book', methods=["POST", "GET"])
def join_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/authors/{request.form['author_id']}")
