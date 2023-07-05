# import libraries to redirect to different page layouts
from flask import Flask, render_template, request, redirect, url_for

import psycopg2
import yaml

# library to randomly redirect users
import random

app = Flask(__name__)

# more classes added upon instructions
classes = [
        "CIS 1001",
        "STAT 1001",
        "MATH 1001",
    ]
#connect DATABSE
db = yaml.safe_load(open('db.yaml'))
conn = psycopg2.connect(
        host= db['postgres_host'],
        database= db["postgres_db"],
        user= db["postgres_user"],
        password= db['postgres_password'])



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET": 
        return render_template("index.html",classes=classes)

    elif request.method == "POST":
        # generate a random number between 0 and 1
        random_number = random.random()

        if random_number < 0.9:
            # run plain_text
            return render_template("/plain_text/plain_text.html",classes=classes)
        else:
            # run visualization
            return render_template("/visualization/visualization.html",classes=classes)

@app.route("/plain_text")
def plain_text():
    return render_template("plain_text.html")

@app.route("/visualization")
def visualization():
    return render_template("visualization.html")

if __name__ == '__main__':
    #so that it keep refresing
    app.run(debug=True)