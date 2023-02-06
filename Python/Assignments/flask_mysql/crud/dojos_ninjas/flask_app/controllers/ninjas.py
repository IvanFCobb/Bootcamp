from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/new')
def new():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', all_dojos=dojos)


@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        "dojo_id": request.form["dojo_id"],
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
    }
    Ninja.create_ninja(data)
    return redirect('/dojos/{}'.format(data["dojo_id"]))


@app.route('/ninjas/edit/<int:num>', methods=["POST", "GET"])
def edit_ninja_page(num):
    dojos = Dojo.get_all()
    ninja = Ninja.get_one(num)
    return render_template('edit_ninja.html', ninja=ninja, all_dojos=dojos)


@app.route('/update_ninja/<int:num>', methods=["POST"])
def update_ninja(num):
    print("before update")
    data = {
        "dojo_id": request.form["dojo_id"],
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
    }
    Ninja.edit_ninja(data, num)
    print("after update")
    return redirect('/dojos/{}'.format(data["dojo_id"]))


@app.route('/ninjas/delete/<int:num>', methods=["POST", "GET"])
def delete_ninja(num):
    ninja = Ninja.get_one(num)
    print(ninja.dojos_id)
    Ninja.delete_ninja(num)
    return redirect('/dojos/{}'.format(ninja.dojos_id))
