import requests
from flask import Flask

app = Flask(__name__)

@app.route("/choice/<planet_name>")
def funk_1(planet_name):
    try:
        response = requests.get(f"https://api.le-systeme-solaire.net/rest/bodies/{planet_name}").json()
    except Exception:
        return "Объект не существует или находится вне Солнечной системы"
    with open("Варианты выбора.html") as f:
        text = f.read()
        text = text.replace("NAME", str(response["englishName"]))
        text = text.replace("MASS", str(response["mass"]["massValue"]))
        text = text.replace("VOL", str(response["vol"]["volValue"]))
        text = text.replace("GRAVITY", str(response["gravity"]))
        text = text.replace("DENSITY", str(response["density"]))
        return text

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")