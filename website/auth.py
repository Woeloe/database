from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import Users

auth = Blueprint("auth", __name__)

@auth.route("/login",  methods=["GET", "POST"])
def account():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = Users.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash("logged in succesfull", category="info")
                login_user(user, remember=True)
                return redirect(url_for("pages.account", naam=current_user.username))
            else:
                flash("incorrect password", category="error")
        else:
            flash("user does not exist!!", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("pages.home"))


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        #get form information
        user = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        usercheck = Users.query.filter_by(email=email).first()
        if usercheck:
            flash("you already have an account with this email", category="error")
        elif(len(email) < 4):
            flash("email", category="error")
        elif(len(password1) < 7):
            flash("password must be at least 7 characters", category="error")
        elif(password1 != password2):
            flash("Passwords don't match", category="error")
        else:
            #sign up
            newUser = Users(username=user, email=email, password=generate_password_hash(password1, method="md5"))
            db.session.add(newUser)
            db.session.commit()
            login_user(newUser, remember=True)
            flash("signed up and logged in succesfull", category="info")
            return redirect(url_for("pages.account", naam=current_user.username))

    return render_template("signup.html", user=current_user)
    


