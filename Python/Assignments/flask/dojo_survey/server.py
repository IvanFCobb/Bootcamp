from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=['POST', 'GET'])
def data():
    print("Got Post Info")

    session['userName'] = request.form['username']
    session['userLocation'] = request.form['location']
    session['userLanguage'] = request.form['language']
    session['userComments'] = request.form['comments']
    return redirect('/results')


@app.route('/results')
def show_data():
    print(session)
    return render_template('results.html')


if __name__ == "__main__":
    app.run(debug=True)
