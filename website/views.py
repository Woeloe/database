# from flask import Blueprint, redirect, render_template, request 
# from main import *

# app = Flask(__name__)

# @app.route("/", methods=["POST", "GET"])
# def home():
#     if(request.form.get("login") == "Login"):
#         naam = request.form.get("naam")
#         return redirect(f"/{naam}")
#     if(request.form.get("create") == "Create"):
#         naam = request.form.get("naam")
#         createUser(naam)
#     return render_template("index.html")

# @app.route("/<naam>", methods=["POST", "GET"])
# def user(naam):
#     pics = download(naam)
#     if(request.form.get("upload") == "uploaden"):
#         path = request.files["image"]
#         print(path)
#         print(path.filename)
#         print(path.name)
#         upload(path, naam)
#         return redirect(f"/{naam}")
    
#     if(request.form.get("delete") is not None):
#         url = request.form.get("url")
#         delete(url, naam)
#         return redirect(f"/{naam}")
#     return render_template("user.html", naam = naam , pics = pics)

# if __name__ == "__main__":
#     app.run(debug=True)
