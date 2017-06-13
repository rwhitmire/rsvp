# pylint: disable=C0103
""" fetch data from firebase and output csv """

import os
import csv
import pyrebase


firebase = pyrebase.initialize_app({
    'apiKey': os.environ['RSVP_FIREBASE_KEY'],
    'authDomain': 'rsvp-2ab3a.firebaseapp.com',
    'databaseURL': 'https://rsvp-2ab3a.firebaseio.com',
    'storageBucket': 'rsvp-2ab3a.appspot.com'
})

rsvps = firebase.database().child('rsvps').get()


with open('out.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for rsvp in rsvps.each():
        key = rsvp.key()
        for guest in rsvp.val():
            writer.writerow([key, guest['name'], guest['meal']])
