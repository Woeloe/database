from turtle import down
from flask import Blueprint, render_template, redirect, request
from flask_login import current_user, login_required
from .cloudinary_api import *
from . import db
from .models import Users

pages = Blueprint("pages", __name__)

@pages.route("/")
def home():
    return render_template("home.html")


@pages.route("/<naam>", methods=["POST", "GET"])
@login_required
def account(naam):
    residents = [current_user.resident1, current_user.resident2, current_user.resident3]
    picsList = [download(residents[0]), download(residents[1]), download(residents[2])]

    print(residents)

    info = zip(residents, picsList)

    if(request.form.get("manageResidents") is not None):
        return redirect(f"/{naam}/bewoners")
    
    if(request.form.get("upload") is not None):
        resident = request.form.get("upload")
        path = request.files["image"]
        upload(path, resident)
        return redirect(f"/{naam}")
    
    if(request.form.get("delete") is not None):
        resident = request.form.get("delete")
        url = request.form.get("url")
        print(resident)
        delete(url, resident)
        return redirect(f"/{naam}")
    return render_template("user.html", naam = naam , info = info)

@pages.route("/<naam>/bewoners", methods=["POST","GET"])
@login_required
def manageResidents(naam):
    residents = [current_user.resident1, current_user.resident2, current_user.resident3]
    numbers = ["1", "2", "3"]
    
    residents = zip(residents, numbers)

    if(request.form.get("save") is not None):
        resident1 = request.form.get("resident1")
        resident2 = request.form.get("resident2")
        resident3 = request.form.get("resident3")

        user_updated = Users.query.filter_by(username=naam).update(dict(resident1 = resident1, resident2 = resident2, resident3 = resident3))
        db.session.commit()

        for resident in [resident1, resident2, resident3]:
            createUser(resident)


        return redirect(f"/{naam}")

    return render_template("manageResidents.html", naam=naam, residents=residents)