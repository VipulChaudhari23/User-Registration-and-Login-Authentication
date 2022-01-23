from flask import Flask, render_template, redirect, request

app = Flask(__name__)

all_details = []

@app.route("/")
def index():
    name = "Enter valid email password"
    print(request.path)
    return render_template("index1.html", name=name, details=all_details)

@app.route("/details/add", methods=["POST"])
def login():
    mail = request.form.get("mail")
    password = request.form.get("password")
    all_details.append(mail)
    all_details.append(password)

    return redirect("/")

@app.route("/details/show")
def show_details():
    return render_template("display.html", details=all_details)
