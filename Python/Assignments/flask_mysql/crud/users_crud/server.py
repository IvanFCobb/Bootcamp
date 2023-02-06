from flask import Flask, render_template, session, redirect, request
from users import User

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template('index.html', all_users=users)


@app.route('/new')
def new():
    return render_template('new.html')


@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.create_user(data)
    return redirect('/')


@app.route('/<int:num>/edit', methods=["POST"])
def edit_user_page(num):
    user = User.get_one(num)
    print(user)
    return render_template('edit.html', user=user)


@app.route('/<int:num>/edit/update', methods=["POST"])
def update_user(num):
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    user = User.edit_user(data, num)
    print(user)
    return redirect('/')


@app.route('/<int:num>/delete', methods=["POST"])
def delete_user(num):
    User.delete_user(num)
    return redirect('/')


@app.route('/<int:num>', methods=["POST"])
def show_user(num):
    user = User.get_one(num)
    print(user)
    return render_template('show.html', user=user)


if __name__ == "__main__":
    app.run(debug=True)
