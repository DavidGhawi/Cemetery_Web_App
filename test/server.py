import os
from flask import Flask, redirect, request,render_template, jsonify
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


@app.route("/login", methods=['GET'])
def login():
    if request.method == 'GET':
        return render_template('Signin.html')


@app.route("/signup", methods=['GET'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')

@app.route("/home")
def redirectToStatic():    
    print("Grab something from static (redirect)")    
    return render_template("Wireframe.html")


if __name__ == "__main__":
    app.run(debug=True)
