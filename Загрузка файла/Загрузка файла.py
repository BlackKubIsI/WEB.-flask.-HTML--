from crypt import methods
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def funk_1():
    with open("Загрузка файла.html") as f:
        text = f.read()
        if request.method == "GET":
            text = text.replace("PATH", "static/img/image.jpg")
        elif request.method == "POST":
            text = text.replace("PATH", "static/img/" + request.form.get("path"))
            print(request.form.get("path"))
        return text

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")