import json

data = {
    "nom": "Dupont",
    "age": 30,
    "ville": "Paris"
}

with open(".\data.json", 'w') as f:
    json.dump(data, f)
