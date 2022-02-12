from flask import Flask

app = Flask(__name__)

@app.route("/")
def funk_1():
    with open("Пейзажи Марса.html") as f:
        return f.read()

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")