from flask import Blueprint, render_template, redirect, request
from flask_login import login_required
from .cloudinary_api import *

pages = Blueprint("pages", __name__)

@pages.route("/")
def home():
    return render_template("home.html")


@pages.route("/<naam>", methods=["POST", "GET"])
@login_required
def account(naam):
    pics = download(naam)
    if(request.form.get("upload") == "uploaden"):
        path = request.files["image"]
        print(path)
        print(path.filename)
        print(path.name)
        upload(path, naam)
        return redirect(f"/{naam}")
    
    if(request.form.get("delete") is not None):
        url = request.form.get("url")
        delete(url, naam)
        return redirect(f"/{naam}")
    return render_template("user.html", naam = naam , pics = pics)