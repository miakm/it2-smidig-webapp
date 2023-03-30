from flask import Flask, render_template, request, jsonify
from quiz import hent_spm
import random
from taylor import hent_swift

app = Flask(__name__)

spm = hent_spm()
quotes = hent_swift()

@app.route("/")
def index():
    quote = quotes["quote"]
    sang = quotes["song"]
    album = quotes["album"]
    if album == "Taylor Swift":
        year = 2006
    elif album == "Fearless":
        year = 2008
    elif album == "Speak Now":
        year = 2010
    elif album == "Red":
        year = 2012
    elif album == "1989":
        year = 2014
    elif album == "Reputation":
        year = 2017
    elif album == "Lover":
        year = 2019
    elif album == "Folklore":
        year = 2020
    elif album == "Evermore":
        year = 2021
    elif album == "Midnights":
        year = 2022
    return render_template("index.html", quote = quote, sang = sang, album = album, year = year)

@app.route("/questions")
def rute_spm():
    alle_svar = spm["feil_svar"] + [spm["svar"]]
    random.shuffle(alle_svar)
    return render_template("questions.html", spm=spm, alle_svar=alle_svar)

# @app.route('/check_answer', methods=['POST'])
# def check_answer():
#     answer = request.form['answer']
#     if answer == 'correct':
#         return jsonify({'result': 'success'})
#     else:
#         return jsonify({'result': 'failure'})

app.run(debug=True)
