import os
import sqlite3
import json
import copy
from flask import Flask, redirect, request, render_template, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
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
            Username = request.form.get('username', default="Error").lower()
            Password = request.form.get('password', default="Error")
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute(
                "SELECT Password FROM Login WHERE Username=?;", [Username])
            data = cur.fetchone()
            if data is not None:
                if check_password_hash(data[0], Password):
                    return render_template('user_upload.html')

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
        Username = request.form.get('Username', default="Error").lower()
        Password = request.form.get('Password', default="Error")
        Password = generate_password_hash(Password)
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO Login ('Username', 'Password')\
                    VALUES (?,?)", (Username, Password))

        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()

        count = cur.execute(
            "SELECT COUNT (*) FROM Login WHERE Username = ?", (Username,)).fetchone()[0]

        if count > 0:
            return render_template('signup.html', message="Username already registered.")

        cur.execute("INSERT INTO Login ('Username', 'Password')\
                    VALUES (?,?)", (Username, Password))

        conn.commit()
        conn.close()
        return redirect("/login")




@app.route("/form", methods=['GET', 'POST'])
def gravesearch():
    if request.method == 'GET':
        return render_template('Forum_page.html')
    if request.method == 'POST':
        name = ""
        try:
            Name = request.form.get('Name', default="Error")
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            data = cur.execute("SELECT [Name],[Date of birth],[Date of death],[Information],[Cemetery section],[Grave number],[Image] FROM Information WHERE Public = 1 and Name = ?;", (Name,))
            for i in data:
                name = i[0]
                DoB = i[1]
                DoD = i[2]
                Info = i[3]
                Csect = i[4]
                Gsect = i[5]
                Img = i[6]

            if len(name) > 0:
                print("yay")
                return render_template("Information_Page.html", name = name, DoB = DoB, DoD = DoD, Info = Info, Csect = Csect, Gsect = Gsect, Img = Img)
            else:
                return redirect('/nodata')
        except Exception as e:
            print(e)
            print('there was an error')
            conn.close()
        finally:
            conn.close()

@app.route("/plots", methods=['GET', 'POST'])
def plots():
    if request.method == 'GET':
        return render_template('plots.html')
    if request.method == 'POST':
        try:
            print ("hi")
            plot = request.form.get('Name', default="Error")
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT [Name], [ID], [Grave number] FROM Information WHERE Public = 1 and [Cemetery section] = ?;", (plot,))
            data = cur.fetchall()
            print("data")
            if len(data) > 0:
                print("yay")
                return render_template("plots.html", data = data)
            else:
                return redirect('/nodata')
        except Exception as e:
            print(e)
            print('there was an error')
            conn.close()
        finally:
            conn.close()

@app.route("/infoPage", methods=['GET'])
def infoPage():
    if request.method == 'GET':
        return render_template("Information_Page.html")




@app.route("/api/map", methods=['GET'])
def api_map():
    mapdata = copy.deepcopy(mapconfig)
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT [ID],[Name],[Date of birth],[Date of death],[Information],[Cemetery section],[Grave number],[Image],[Latitude],[Longitude] FROM Information WHERE Public = 1 and Latitude NOT NULL and Longitude NOT NULL;")
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
    data = c.fetchone()
    conn.close()
    infodata = {}
    if data is not None:
        infodata = {
            "name": data[0],
            "dob": data[1],
            "dod": data[2],
            "info": data[3],
            "cs": data[4],
            "gn": data[5],
            "img": data[6]
        }

    return jsonify(infodata)


@app.route("/livemap", methods=['GET'])
def livemap():
    return render_template('geomap.html')


if __name__ == "__main__":
    app.run(debug=True)
