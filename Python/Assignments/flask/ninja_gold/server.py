from flask import Flask, render_template, session, redirect, request
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/', methods=['POST', 'GET'])
def index():
    if "winMessage" not in session:
        session['winMessage'] = ""
    if "restButton" not in session:
        session['resetButton'] = ""
    if "activityLog" not in session:
        session['activityLog'] = ""
    if "totalGold" not in session:
        session['totalGold'] = 0
    if session['totalGold'] < 0:
        session['totalGold'] = 0
    if session['totalGold'] > 100:
        session['winMessage'] = "<h2 class='win'>WINNER!!!!</h2>"
        session['resetButton'] = "<a class='btn btn-danger text-center mx-2 mt-3' href='/destroy_session'>Restart Game</a>"
    print(session)
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():
    now = datetime.now()
    print("Current date and time : ")
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    temp_log = session['activityLog']
    session['activityLog'] = ""
    if "activityLog" not in session:
        session['activityLog'] = "<p>Hello!</p>"
    if request.form['which_activity'] == 'Farm':
        randomNumber = random.randint(10, 20)
        session['totalGold'] = session['totalGold'] + randomNumber
        session['activityLog'] += "<p class='win'>Earned %s gold from the farm! %s</p>" % (
            randomNumber, current_time)
        session['activityLog'] += temp_log
    if request.form['which_activity'] == 'Cave':
        randomNumber = random.randint(5, 10)
        session['totalGold'] = session['totalGold'] + randomNumber
        session['activityLog'] += "<p class='win'>Earned %s gold from the cave! %s</p>" % (
            randomNumber, current_time)
        session['activityLog'] += temp_log
    if request.form['which_activity'] == 'House':
        randomNumber = random.randint(2, 5)
        session['totalGold'] = session['totalGold'] + randomNumber
        session['activityLog'] += "<p class='win'>Earned %s gold from the house! %s</p>" % (
            randomNumber, current_time)
        session['activityLog'] += temp_log
    if request.form['which_activity'] == 'Casino':
        randomNumber = random.randint(-50, 50)
        if randomNumber > 0:
            session['totalGold'] = session['totalGold'] + randomNumber
            session['activityLog'] += "<p class='win'>Entered a casino and won %s gold from the casino! %s</p>" % (
                randomNumber, current_time)
            session['activityLog'] += temp_log
        else:
            session['totalGold'] = session['totalGold'] + randomNumber
            session['activityLog'] += "<p class='lose'>Entered a casino and lost %s gold from the casino... Ouch. %s</p>" % (
                randomNumber, current_time)
            session['activityLog'] += temp_log
    print(session)
    return redirect('/')


@ app.route('/destroy_session', methods=['POST', 'GET'])
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
