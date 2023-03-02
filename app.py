from flask import Flask, render_template
from quiz import hent_spm
import random

app = Flask(__name__)

spm = hent_spm()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/questions")
def rute_spm():
    alle_svar = spm["feil_svar"] + [spm["svar"]]
    random.shuffle(alle_svar)
    return render_template("questions.html", spm=spm, alle_svar=alle_svar)

app.run(debug=True)
