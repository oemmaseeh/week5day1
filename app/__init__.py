from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/html")
def index_html():
    python_people = ["Lil Baby", "Lil Wayne", "Moneybag Yo", "Pop Smoke", "The Weekend"]
    return render_template("index.html", message="hello from my template", red = True, html_people=python_people)

@app.route("/json")
def json():
    return{"message":"Hello from my api"}

