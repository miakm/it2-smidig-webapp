from flask import Flask, render_template
from quiz import hent_data

app = Flask(__name__)

spm = hent_data()

@app.route("/")
def index():
    navn = "Sandvika"
    return render_template("index.html", navn=navn)

@app.route("/questions")
def index():
    return render_template("questions.html", spm=spm)

app.run(debug=True)