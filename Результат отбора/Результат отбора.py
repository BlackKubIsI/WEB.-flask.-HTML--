from flask import Flask

app = Flask(__name__)

@app.route("/results/<nickname>/<int:level>/<float:rating>")
def funk_1(nickname, level, rating):
    with open("Результат отбора.html") as f:
        text = f.read()
        text = text.replace("NICKNAME", nickname)
        text = text.replace("LEVEL", str(level))
        text = text.replace("RATING", str(rating))
        return text

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")