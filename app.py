# pylint: disable=C0103
""" Web server for wedding RSVPs. """

import os
import pyrebase
from flask import Flask, render_template, request, redirect


app = Flask(__name__, static_url_path='')

firebase = pyrebase.initialize_app({
    'apiKey': os.environ['RSVP_FIREBASE_KEY'],
    'authDomain': 'rsvp-2ab3a.firebaseapp.com',
    'databaseURL': 'https://rsvp-2ab3a.firebaseio.com',
    'storageBucket': 'rsvp-2ab3a.appspot.com'
})

db = firebase.database()


if __name__ != '__main__':
    @app.before_request
    def force_https():
        """ Force https in production """
        if request.url.startswith('http://'):
            print('called')
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)


@app.route('/')
def index():
    """ Home route """
    return render_template('index.html')


@app.route('/rsvp', methods=['POST'])
def rsvp():
    """ Receives RSVPs """
    data = request.get_json()
    db.child('rsvps').push(data)
    return ('', 204)


if __name__ == '__main__':
    app.run(debug=True)
