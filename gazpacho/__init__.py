from flask import Flask, render_template, request, session, url_for, redirect, flash, send_file
from util import db
# from util import exceptions
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

DIR = os.path.dirname(__file__) or '.'
DIR += '/'
DB_PATH = DIR + 'data/block.db'
print(DB_PATH)
# Database setup
store = db.Database(DB_PATH)
TABLES = {
    'users': ['user TEXT PRIMARY KEY', 'first TEXT', 'last TEXT', 'password TEXT', 'salary INTEGER', 'POSITION TEXT', 'HOURS TEXT', 'DAYS TEXT'],
    'projects': ['id INTEGER', 'name TEXT PRIMARY KEY', 'creator TEXT'],
    'record' : ['target TEXT', 'initated_by TEXT', 'type TEXT', 'description TEXT', 'id INTEGER', 'timeStamp INTEGER', 'message TEXT', 'view_level INTEGER']
}
for name, cols in TABLES.items():
    # print(name, cols)
    state = store.createTable(name, *cols)
    # print(state)

@app.route("/")
def index():
    print( session.get('username') )
    if session.get('username') != None:
        return redirect(url_for("home"))
    return render_template("welcome.html")

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
        session['username'] = name
        return redirect(url_for("home"))
    else:
        # print("FLASH")
        flash("The username and password do not match")
        return redirect(url_for("login"))

@app.route("/auth_register", methods=['POST'])
def auth_register():
    form = request.form
    # print(form)
    if store.insertUser(form):
        return redirect(url_for("home"))
    else:
        flash("Username is already taken")
        return redirect(url_for("register"))
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/home")
def home():
    username=session.get('username')
    if username == None:
        return redirect(url_for("index"))
    return render_template("home.html",user=username)

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/task")
def task():
    return render_template("task.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
