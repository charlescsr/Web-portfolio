from flask import Flask, render_template, request, redirect
import datetime
from flask_pymongo import pymongo

app = Flask(__name__)
app.secret_key = '?A7_`a?^k=9+1k6Z@XX0vFpDasd"pQ'
CONNECTION_STRING = "mongodb+srv://charles:0QyVtWs73CMc6DHe@csr-personal.qfh5r.mongodb.net/db_personal?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
main_db = client['db_personal']['visits']

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/resume")
def resume():
    return render_template("cv.html")


@app.route("/projects")
def projects():
    return render_template("projects-grid-cards.html")


@app.route("/certificates")
def certificates():
    return render_template("certificates.html")

@app.route("/the-big-one")
def the_big_one():
    return render_template("the-big-one.html")

@app.route("/apb")
def apb():
    return render_template("apb.html")

@app.route("/contactme")
def contact():
    return render_template("contact.html")

@app.route("/mail", methods=["POST"])
def send():
    name = request.form["name"]
    email = request.form["email"]
    sub = request.form["subject"]
    mess = request.form["message"]

    final_value = {'name': name, 'email': email, 'subject': sub, 'message': mess, 'time_stamp': datetime.datetime.now()}

    main_db.insert_one(final_value)
    
    return redirect("mailto:rcharles.samuel99@gmail.com?subject="+str(sub)+"&body="+str(mess))

if __name__ == '__main__':
    app.run(host='0.0.0.0')