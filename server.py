import os
import sqlite3
import json
import copy
from flask import Flask, redirect, request, render_template, jsonify
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

DATABASE = 'cemetery_db.db'

if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    script = open('cemetery_database.sql', 'r').read()
    c.executescript(script)
    conn.commit()
    conn.close()

mapconfig = json.load(open("mapconfig.json"))

app = Flask(__name__)


@app.route("/signup", methods=['GET'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')


@app.route("/home", methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('Home_page.html')


@app.route("/map", methods=['GET'])
def map():
    if request.method == 'GET':
        return render_template('map_page.html')


@app.route("/nodata", methods=['GET'])
def nodata():
    if request.method == 'GET':
        return render_template('nodata.html')


@app.route("/moderator", methods=['GET'])
def moderator():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM Information WHERE Public = 0;")
    data = c.fetchall()

    return render_template('moderator.html', information=data)


@app.route("/remove/<id>", methods=['POST'])
def remove(id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("DELETE FROM Information WHERE ID = ?", (id,))
    conn.commit()
    conn.close()
    return "ok"


@app.route("/approve/<id>", methods=['POST'])
def approve(id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("UPDATE Information SET Public = 1 WHERE ID = ?", (id,))
    conn.commit()
    conn.close()
    return "ok"


@app.route("/add", methods=['GET', 'POST'])
def add_render():
    if request.method == 'GET':
        return render_template('user_upload.html')
    else:
        name = request.form.get('name')
        Dbirth = request.form.get('Dbirth')
        Ddeath = request.form.get('Ddeath')
        Information = request.form.get('Information')
        Cemetery_section = request.form.get('Cemetery_section')
        Grave_number = request.form.get('Grave_number')
        Image = ""
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("INSERT INTO Information('Name', 'Date of birth', 'Date of death', 'Information', 'Cemetery section', 'Grave number', 'Image', 'Public') VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
                  (name, Dbirth, Ddeath, Information, Cemetery_section, Grave_number, Image, 0))
        conn.commit()
        conn.close()
        return render_template('user_upload.html', message="Submitted data for review!")


@app.route("/login", methods=['GET', 'POST'])
def usersearch():
    if request.method == 'GET':
        return render_template('Signin.html')
    if request.method == 'POST':
        try:
            Username = request.form.get('username', default="Error")
            Password = request.form.get('password', default="Error")
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM Login WHERE Username=? AND Password=?;", [Username, Password])
            data = cur.fetchall()
            if len(data) > 0:
                return redirect('/home')
            else:
                return render_template('Signin.html', message="Wrong Username or Password")
        except Exception as e:
            print(e)
            print('there was an error')
            conn.close()
        finally:
            conn.close()
            # return render_template('ListStudents.html', data = data)


@app.route("/signup", methods=['POST', 'GET'])
def createuser():
    if request.method == 'GET':
        return render_template('signup.html')
    if request.method == 'POST':
        # rem: args for get form for post
        Username = request.form.get('Username', default="Error")
        Password = request.form.get('Password', default="Error")
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO Login ('Username', 'Password')\
						VALUES (?,?)", (Username, Password))

            conn.commit()
            msg = "Record successfully added"
        except:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return msg


@app.route("/api/map", methods=['GET'])
def api_map():
    mapdata = copy.deepcopy(mapconfig)
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT ID,Name,'Date of birth','Date of death',Information,'Cemetery section','Grave number',Image,Latitude,Longitude FROM Information WHERE Public = 1 and Latitude NOT NULL and Longitude NOT NULL;")
    data = c.fetchall()
    for row in data:
        mapdata['markers'].append({
            "id": row[0],
            "name": row[1],
            "dob": row[2],
            "dod": row[3],
            "info": row[4],
            "cs": row[5],
            "gn": row[6],
            "img": row[7],
            "lat": row[8],
            "lng": row[9]
        })
    conn.close()

    return jsonify(mapdata)


@app.route("/api/information/<id>", methods=['GET'])
def api_information(id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT Name,'Date of birth','Date of death',Information,'Cemetery section','Grave number',Image FROM Information WHERE ID = ?;", (id,))
    data = c.fetchall()
    conn.close()
    infodata = []
    for row in data:
        infodata.append({
            "name": row[0],
            "dob": row[1],
            "dod": row[2],
            "info": row[3],
            "cs": row[4],
            "gn": row[5],
            "img": row[6]
        })
    return jsonify(infodata)


if __name__ == "__main__":
    app.run(debug=True)
