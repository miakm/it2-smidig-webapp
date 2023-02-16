from flask import Flask, render_template
from quiz import hent_spm


app = Flask(__name__)

spm = hent_spm()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/questions")
def rute_spm():
    return render_template("questions.html", spm=spm)

app.run(debug=True)