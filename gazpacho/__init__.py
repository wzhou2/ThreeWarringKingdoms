from flask import Flask, render_template, request, session, url_for, redirect, flash, send_file
from util import db
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

# Database setup
store = db.Database("data\\block.db")
TABLES = {
    'users': ['user TEXT', 'first TEXT', 'last TEXT', 'password TEXT', 'salary INTEGER', 'POSITION TEXT', 'HOURS TEXT', 'DAYS TEXT'],
    'projects': ['id INTEGER', 'name TEXT', 'creator TEXT'],
    'record' : ['target TEXT', 'initated_by TEXT', 'type TEXT', 'description TEXT', 'id INTEGER', 'timeStamp INTEGER', 'message TEXT', 'view_level INTEGER']
}
for name, cols in TABLES.items():
    # print(name, cols)
    state = store.createTable(name, *cols)
    # print(state)

@app.route("/")
def index():
    return render_template("landing.html")

@app.route("/login_register")
def login_register():
    return render_template("login_register.html")

@app.route("/auth_login", methods=['POST'])
def auth_login():
    print( request.form )
    return "auth login"

@app.route("/auth_register", methods=['POST'])
def auth_register():
    return "auth register"

@app.route("/project")
def project():
    return render_template("project.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
