import os
from flask import Flask, render_template, request, session, url_for, redirect, flash, send_file
from util import db
from util.constants import *

app = Flask(__name__)
app.secret_key = os.urandom(32)

DIR = os.path.dirname(__file__) or '.'
DIR += '/'
DB_PATH = DIR + 'data/block.db'
# DB_PATH = DIR + 'util/test.db'
print(DB_PATH)
# Database setup

store = db.Database(DB_PATH)

for name, cols in TABLES.items():
    # print(name, cols)
    state = store.createTable(name, *cols)
    # print(state)
#home,login,register
@app.route("/")
def index():
    """Returns the welcome page if there is
    a user in session, otherwise return the
    register/login page.
    """
    # print( session.get('username') )
    if session.get(USER) != None:
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
    name = request.form[USER]
    pd = request.form[PASSWORD]
    # print(name, pd)
    if store.verifyUser(name, pd):
        session[USER] = name
        session[POSITION] = ACCESS[store.getPosition(name)]
        return redirect(url_for("home"))
    else:
        # print("FLASH")
        flash("The username and password do not match")
        return redirect(url_for("index"))

@app.route("/auth_register", methods=['POST'])
def auth_register():
    """ Inserts the user into database if valid
    """
    form = request.form
    name = form[USER]
    if store.insertUser(form):
        session[USER] = name
        session[POSITION] = ACCESS[store.getPosition(name)]
        return redirect(url_for("home"))
    else:
        flash("Username is already taken")
        return redirect(url_for("index"))

@app.route('/logout')
def logout():
    """ Logs the user out and clears the session info
    """
    session.clear()
    return redirect(url_for("index"))

@app.route("/home")
def home():
    # print( session.get('username') )
    # print( session['username'] )
    # print( session )
    if session.get(USER) == None:
        return redirect(url_for("index"))
    projects = store.getProjects(session[USER])
    return render_template("home.html")
#projects
@app.route("/project")
def project():
    """ Returns the project page
    """
    if session.get(USER) == None:
        return redirect(url_for("index"))
    return render_template("project.html")

@app.route("/create_project")
def create_project():
    """ determines project status
    """
    return render_template("create_project.html",employees=store.getAllEmployees())

@app.route("/create", methods=['POST'])
def create():
    form = request.form
    name=form["name"]
    record=''
    if store.createProject(name,session[USER],record):#
        store.addMembers(name,request.form.getlist('workers'))
        pass
    else:
        return redirect(url_for("project"))

#account
@app.route("/account")
def account():
    """ Returns the account page
    """
    if session.get(USER) == None:
        return redirect(url_for("index"))
    return render_template("account.html", info = store.getUser(session[USER]))

##    if store.get('block.db',session[USER],salary,WHERE salary != 0):
##        return render_template("account.html")
##    return render_template("account.html",editable=True)

@app.route("/task")
def task():
    """ Return the task creation page
    """
    if session.get(USER) == None:
        return redirect(url_for("index"))
    return render_template("task.html")

@app.route("/schedule")
def schedule():
    """Return the schedule page
    """
    return render_template("schedule.html")

@app.route("/inbox")
def inbox():
    """Return the messages
    """
    return render_template("inbox.html",messages=False)

@app.route("/getHTML")
def getForms():
    """Returns the form requested by ajax
    """
    type = request.args['type']

    return render_template("{}.html".format(type))



if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
