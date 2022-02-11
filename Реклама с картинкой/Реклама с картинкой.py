from flask import Flask

app = Flask(__name__)

@app.route("/promotion_image")
def funk_1():
    with open("Реклама с картинкой.html") as f:
        return f.read()

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")