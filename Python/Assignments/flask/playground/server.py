from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/play")
def box():
    return render_template("play.html", num=3, color="blue")


@app.route("/play/<int:num>")
def boxes(num):
    return render_template("play.html", num=num, color="blue")


@app.route("/play/<int:num>/<color>")
def boxeColors(num, color):
    return render_template("play.html", num=num, color=color)


# @app.route("/play/<int:num>")
# def hello(item, num):
#     return render_template("play.html", item=item, num=num)


if __name__ == "__main__":
    app.run(debug=True)
