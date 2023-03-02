import random
from random import randint
import requests

url = f"https://opentdb.com/api.php?amount=10&category=23&type=multiple"
resultat = requests.get(url)
data = resultat.json()
i = randint(1,10)

spm = {
    "sporsmaal": data["results"][i]["question"],
    "svar": data["results"][i]["correct_answer"],
    "feil_svar": data["results"][i]["incorrect_answers"]
}

alle_svar = spm["feil_svar"] + [spm["svar"]]
print(alle_svar)
shuffle = random.shuffle(alle_svar)
print(alle_svar)