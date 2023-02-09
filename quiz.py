import requests

def hent_data():
    url = f"https://opentdb.com/api.php?amount=10&category=23&type=multiple"
    resultat = requests.get(url)
    data = resultat.json()
    return data

def hent_spm():
    data = hent_data()
    pass
