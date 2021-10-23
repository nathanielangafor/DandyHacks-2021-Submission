import json
import sqlite3
from flask import Flask, request
app = Flask(__name__)
app.secret_key = b"Da ya biezlikiy patamy shto u menya nie litso"

def userTable():
    conn = sqlite3.connect(r"/Users/n8/Desktop/DandyHacks/database.db")

    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Users (email TEXT, username TEXT, password TEXT, points INETEGER, achievements TEXT)')

def locationTable():
    conn = sqlite3.connect(r"/Users/n8/Desktop/DandyHacks/database.db")

    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Locations (user TEXT, longitude TEXT, latitude TEXT, image TEXT, comment TEXT, type INTEGER, title TEXT)')


@app.route('/insertUser/', methods=['GET', 'POST'])
def insertUser():
    if request.method == 'POST':
        conn = sqlite3.connect(r"/Users/n8/Desktop/DandyHacks/database.db")

        achievements = {
            "beHuman": ["Be Human", False, "You are human!", 100],
            "environmentalist": ["Environmentalist", False, "You completed your first cleanup activity!", 100],
            "warrior": ["Warrior", False, "You completed your first 5 cleanup activities!", 300],
            "cleanupWarlock": ["Cleanup Warlock", False, "You completed your first 10 cleanup activities!", 500],
        }
            
        points = 0

        c = conn.cursor()
        c.execute("INSERT INTO Users (email, username, password, points, achievements) VALUES (?, ?, ?, ?, ?)", (request.form.get('email'), request.form.get('username'), request.form.get('password'), points, achievements,))
        conn.commit()

        return 'True'

@app.route('/insertLocation/', methods=['GET', 'POST'])
def insertLocation():
    if request.method == 'POST':
        conn = sqlite3.connect(r"/Users/n8/Desktop/DandyHacks/database.db")

        c = conn.cursor()
        c.execute("INSERT INTO Locations (user, longitude, latitude, image, comment, type, title) VALUES (?, ?, ?, ?, ?, ?, ?)", (request.form.get('user'), request.form.get('longitude'), request.form.get('latitude'), request.form.get('image'), request.form.get('comment'), request.form.get('type'), request.form.get('title'),))
        conn.commit()

        return 'True'

@app.route('/delete/', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        conn = sqlite3.connect(r"/Users/n8/Desktop/DandyHacks/database.db")

        c = conn.cursor()
        c.execute('DELETE FROM {} WHERE {}=(?)'.format(request.form.get('table'), request.form.get('criteria')), (request.form.get('identifier'),))
        conn.commit()

        return 'True'

@app.route('/read/', methods=['GET', 'POST'])
def read():
    if request.method == 'POST':
        conn = sqlite3.connect(r"/Users/n8/Desktop/DandyHacks/database.db")

        c = conn.cursor()
        c.execute('SELECT * FROM {}'.format(request.form.get('table')))
        data = c.fetchall()
        return str(data)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        conn = sqlite3.connect(r"/Users/n8/Desktop/DandyHacks/database.db")

        c = conn.cursor()
        c.execute('SELECT * FROM Users')
        data = c.fetchall()

        for user in data:
            if user[1] == request.form.get('username'):
                if user[2] == request.form.get('password'):
                    return 'logged in'
                else:
                    return 'invalid password'

        return 'invalid username'


@app.route('/test/', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return 'TEST'

userTable()
locationTable()

if __name__ == "__main__":
    app.run(debug=False)


# Types
# Cleanup