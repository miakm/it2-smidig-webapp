import requests

def hent_spm():
    url = f"https://opentdb.com/api.php?amount=10&category=23&type=multiple"
    resultat = requests.get(url)
    data = resultat.json()
    return data["results"][0]["question"]

def hent_svar():
    url = f"https://opentdb.com/api.php?amount=10&category=23&type=multiple"
    resultat = requests.get(url)
    data = resultat.json()
    return data["results"][0]["correct_answer"]