from flask import Flask, redirect, url_for, render_template, request
import requests
import json

app = Flask(__name__)
user_admin = False


@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        if request.form["password"] == 'password':
            return redirect(url_for("user", usr=user))
        else:
            return render_template("login.html", password_err="incorrect password")
    else:
        return render_template("login.html")


@app.route("/<usr>", methods=["POST", "GET"])
def user(usr):
    cat_image = requests.get("https://aws.random.cat/meow?ref=apilist.fun")
    if request.method == "POST":
        if request.form.get("cat"):
            cat_image = requests.get("https://aws.random.cat/meow?ref=apilist.fun")
    cat_image = json.loads(cat_image.text)
    cat_image = cat_image['file']
    return render_template("usr.html", user=usr, cat_image=cat_image)

if __name__ == "__main__":
    app.run(debug=True)