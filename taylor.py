import requests


def hent_swift():
    url = f"https://taylorswiftapi.onrender.com/get"
    resultat = requests.get(url)
    data = resultat.json()
    return data
