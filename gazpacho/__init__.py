from flask import Flask, render_template, request, session, url_for, redirect, flash, send_file
from util import db
# from util import exceptions
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

# Database setup
store = db.Database("./data/block.db")
TABLES = {
    'users': ['user TEXT PRIMARY KEY', 'first TEXT', 'last TEXT', 'password TEXT', 'salary INTEGER', 'POSITION TEXT', 'HOURS TEXT', 'DAYS TEXT'],
    'projects': ['id INTEGER AUTOINCREMENT', 'name TEXT PRIMARY KEY', 'creator TEXT'],
    'record' : ['target TEXT', 'initated_by TEXT', 'type TEXT', 'description TEXT', 'id INTEGER', 'timeStamp INTEGER', 'message TEXT', 'view_level INTEGER']
}
for name, cols in TABLES.items():
    # print(name, cols)
    state = store.createTable(name, *cols)
    # print(state)

@app.route("/")
def index():
    return render_template("landing.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/auth_login", methods=['POST'])
def auth_login():
    name = request.form['username']
    pd = request.form['pw']
    print(name, pd)
    if store.verifyUser(name, pd):
        return redirect(url_for("project"))
    else:
        flash("The username and password do not match")
        return redirect(url_for("login"))

@app.route("/auth_register", methods=['POST'])
def auth_register():
    form = request.form
    # print(form)
    if store.insertUser(form):
        return redirect(url_for("project"))
    else:
        flash("Username is already taken")
        return redirect(url_for("register"))

@app.route("/project")
def project():
    return render_template("project.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
