from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/', methods=['POST', 'GET'])
def index():
    if "count" not in session:
        session['count'] = 1
    return render_template('index.html')


@app.route('/count', methods=['POST', 'GET'])
def views():
    print("Got Post Info")
    session['count'] = session['count'] + 1
    print(session)
    return redirect('/')


@app.route('/destroy_session', methods=['POST', 'GET'])
def reset():
    session.pop('count')
    print(session)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
