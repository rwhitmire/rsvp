from flask import Flask, render_template, request
import pyrebase
import os

app = Flask(__name__, static_url_path='')


firebase = pyrebase.initialize_app({
  'apiKey': os.environ['RSVP_FIREBASE_KEY'],
  'authDomain': 'rsvp-2ab3a.firebaseapp.com',
  'databaseURL': 'https://rsvp-2ab3a.firebaseio.com',
  'storageBucket': 'rsvp-2ab3a.appspot.com'
})

db = firebase.database()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/rsvp', methods=['POST'])
def rsvp():
    data = request.get_json()
    db.child('rsvps').push(data)
    return ('', 204)


if __name__ == '__main__':
    app.run(debug=True)
