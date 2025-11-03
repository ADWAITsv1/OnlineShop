from flask import Flask, render_template, url_for, redirect, session 
from forms import *
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(32)
app.config["WTF_CSRF_SECRET_KEY"] = os.urandom(32)
app.config["WTF_CSRF_ENABLED"] = True
csrf = CSRFProtect(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        print(form.username.data)
        print(form.password.data)

        if form.password.data != "password":
            session["msg"] = "Username or Password is incorrect."
            return redirect(url_for("login"))

        return redirect(url_for("index"))

    msg = session.get("msg")
    session.pop("msg", None)
    return render_template("login.html", form=form, msg=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
