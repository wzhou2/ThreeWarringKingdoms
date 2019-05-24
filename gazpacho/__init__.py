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
    'users': ['user TEXT PRIMARY KEY', 'first TEXT', 'last TEXT', 'password TEXT', 'salary INTEGER', 'POSITION TEXT'],
    'projects': [ 'name TEXT PRIMARY KEY', 'creator TEXT', 'members TEXT'],
    'schedules': ['user TEXT PRIMARY KEY', 'monday TEXT', 'tuesday TEXT', 'wednesday TEXT', 'thursday TEXT', 'friday TEXT', 'saturday TEXT', 'sunday TEXT'],
    'record' : ['target TEXT', 'initated_by TEXT', 'type TEXT', 'description TEXT', 'id INTEGER', 'timeStamp INTEGER', 'message TEXT', 'view_level INTEGER']
}
for name, cols in TABLES.items():
    # print(name, cols)
    state = store.createTable(name, *cols)
    # print(state)

@app.route("/")
def index():
    """Returns the welcome page if there is
    a user in session, otherwise return the
    register/login page.
    """
    # print( session.get('username') )
    if session.get('username') != None:
        return redirect(url_for("home"))
    return render_template("welcome.html")

@app.route("/login")
def login():
    """ Returns the login form
    """
    return render_template("login.html")

@app.route("/register")
def register():
    """ Returns the register form
    """
    return render_template("register.html")

@app.route("/auth_login", methods=['POST'])
def auth_login():
    """ Verifiy the login information
    """
    name = request.form['username']
    pd = request.form['pw']
    # print(name, pd)
    if store.verifyUser(name, pd):
        session['username'] = name
        return redirect(url_for("home"))
    else:
        # print("FLASH")
        flash("The username and password do not match")
        return redirect(url_for("login"))

@app.route("/auth_register", methods=['POST'])
def auth_register():
    """ Inserts the user into database if valid
    """
    form = request.form
    name = form['user']
    if store.insertUser(form):
        session['username'] = name
        return redirect(url_for("home"))
    else:
        flash("Username is already taken")
        return redirect(url_for("register"))

@app.route('/logout')
def logout():
    """ Logs the user out and clears the session info
    """
    session.pop('username', None)
    return redirect(url_for("index"))

@app.route("/home")
def home():
    # print( session.get('username') )
    # print( session['username'] )
    print( session )
    if session.get('username') == None:
        return redirect(url_for("index"))
    projects = store.getProjects(session['username'])
    return render_template("home.html")

@app.route("/project")
def project():
    """ Returns the project page
    """
    return render_template("project.html")

@app.route("/account")
def account():
    """ Returns the account page
    """
    return render_template("account.html")

@app.route("/task")
def task():
    """ Return the task creation page
    """
    return render_template("task.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
