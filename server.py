import os
import sqlite3
from flask import Flask, redirect, request,render_template, jsonify
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

DATABASE = 'cemetery_db.db'

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
                return redirect('/login')
        except Exception as e:
            print(e)
            print('there was an error')
            conn.close()
        finally:
            conn.close()



@app.route("/signup", methods = ['POST','GET'])
def createuser():
	if request.method =='GET':
		return render_template('signup.html')
	if request.method =='POST':
		Username = request.form.get('Username', default="Error")#rem: args for get form for post
		Password = request.form.get('Password', default="Error")
		print(Username)
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("INSERT INTO Login ('Username', 'Password')\
						VALUES (?,?)",(Username, Password) )

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
