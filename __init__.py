from flask import Flask, render_template, request, session, url_for, redirect, flash, send_file
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def index():
    return render_template("landing.html")

@app.route("/login_register")
def login_register():
    return render_template("login_register.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
