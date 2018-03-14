from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "penguins"
import random, datetime, time
@app.route('/')
def index():
    if not session.get('gold'):
        session['gold'] = 0
    return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def money():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if not session.get('messages'):
        session['messages'] = []
    if request.form['action'] == "farm":
        print "hello"
        n = random.randint(10, 20)
        session['gold'] += n 
        session['messages'].append(("Earned {} gold from the farm ({})".format(n, timestamp), "green"))
    elif request.form['action'] == "cave":
        print "hello"
        n = random.randint(5, 10)
        session['gold'] += n 
        session['messages'].append(("Earned {} gold from the cave! ({})".format(n, timestamp), "green"))
        print session['messages']
    elif request.form['action'] == "house":
        print "hello"
        n = random.randint(2, 5)
        session['gold'] += n
        session['messages'].append(("Earned {} gold from the house! ({})".format(n, timestamp), "green"))
    elif request.form['action'] == "casino":
        print "hello"
        n = random.randint(-50, 50)
        session['gold'] += n
        if n < 0:
            session['messages'].append(("Entered a casino and lost {} gold... Ouch.. ({})".format(n, timestamp), "red"))
        else:
            session['messages'].append(("Earned {} gold from the Casino! ({})".format(n, timestamp), "green"))
        

    return redirect('/')
app.run(debug=True)