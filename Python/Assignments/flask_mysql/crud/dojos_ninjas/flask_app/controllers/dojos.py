from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    return render_template('index.html', all_dojos=dojos)


@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"],
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')


@app.route('/dojos/<int:num>', methods=["POST", "GET"])
def show_dojo(num):
    print("test")
    dojo = Dojo.get_one(num)
    ninjas = Ninja.get_ninjas_in_dojo(num)
    return render_template('show_dojo.html', dojo=dojo, all_ninjas=ninjas)
