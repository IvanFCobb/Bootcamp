from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.order import Order


@app.route('/', methods=["GET"])
def index():
    return redirect('/orders')


@app.route('/orders')
def orders():
    orders = Order.get_all()
    return render_template('orders_page.html', all_orders=orders)


@app.route('/order/new')
def create_order():
    return render_template('new_order.html', all_orders=orders)


@app.route('/create_order', methods=["POST"])
def update_order():
    data = {
        "customer_name": request.form["customer_name"],
        "cookie_type": request.form["cookie_type"],
        "num_of_boxes": request.form["num_of_boxes"],
    }
    if not Order.validate_order(data):
        return redirect('/order/new')
    Order.save(data)
    return redirect('/orders')


@app.route('/order/edit/<int:num>', methods=["POST", "GET"])
def edit_order_page(num):
    order = Order.get_one(num)
    return render_template('update_order.html', order=order)


@app.route('/update_order/<int:num>', methods=["POST"])
def update_oder(num):
    print("before update")
    data = {
        "customer_name": request.form["customer_name"],
        "cookie_type": request.form["cookie_type"],
        "num_of_boxes": request.form["num_of_boxes"],
    }
    if not Order.validate_order(data):
        return redirect('/order/edit/{}'.format(num))
    Order.update_order(data, num)
    print("after update")
    return redirect('/orders')


@app.route('/order/delete/<int:num>', methods=["POST", "GET"])
def delete_order(num):
    Order.delete_order(num)
    return redirect('/orders')
