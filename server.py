import os
import sqlite3
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

app = Flask(__name__)


# @app.route("/login.", methods=['GET'])
# def login():
#     if request.method == 'GET':
#         return render_template('Signin.html')


@app.route("/signup", methods=['GET'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')


@app.route("/home", methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('Home_page.html')

# @app.route("/home")
# def redirectToStatic():
#     print("Grab something from static (redirect)")
#     return render_template("Wireframe.html")

# @app.route('/templates/signup.html', methods = ["post"])
# def admin():
#     username = request.form.get('username')
#     if username == "admin" and password == "admin":
#         return render_template("Wireframe.html")
#     else:
#         message = "Wrong Username"
#         return render_template("login_page.html")


@app.route("/login", methods=['GET', 'POST'])
def usersearch():
    if request.method == 'GET':
        return render_template('Signin.html')
    if request.method == 'POST':
        try:
            Username = request.form.get('username', default="Error")
            print(Username)
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT * FROM Login WHERE Username=?;", [Username])
            data = cur.fetchall()
            print(data)
        except Exception as e:
            print(e)
            print('there was an error')
            conn.close()
        finally:
            conn.close()
            return str("its done")
            # return render_template('ListStudents.html', data = data)


@app.route("/signup", methods=['POST', 'GET'])
def createuser():
    if request.method == 'GET':
        return render_template('signup.html')
    if request.method == 'POST':
        # rem: args for get form for post
        Username = request.form.get('Username', default="Error")
        Password = request.form.get('Password', default="Error")
        print(Username)
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


if __name__ == "__main__":
    app.run(debug=True)
