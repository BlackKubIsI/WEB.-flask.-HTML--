from crypt import methods
from flask import Flask, request

app = Flask(__name__)

prof = "инженер-исследователь, пилот, строитель, экзобиолог, врач, \
    инженер по терраформированию, климатолог, специалист по радиационной\
         защите, астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог,\
              оператор марсохода, киберинженер, штурман, пилот дронов".split(", ")


@app.route("/", methods=["GET", "POST"])
def funk_1():
    if request.method == "GET":
        with open("Отбор астронавтов.html") as f:
            return f.read()
    elif request.method == "POST":
        print("Фамилия " + str(request.form["fam"]))
        print("Имя " + str(request.form["name"]))
        print("Почта " + str(request.form["email"]))
        print("Образование " + str(request.form["Образование"]))
        print("Профессии " + ", ".join([prof[int(i[0][3:]) - 1]
              for i in list(request.form.lists()) if i[0][:2] == "ch"]))
        print("Пол " + str(request.form.get("pol")))
        print("Почему хочет участвовать " + str(request.form["about"]))
        print("Фото " + str(request.form["file"]))
        print("Готовы ли остаться на Марсе" + str(request.form["ost"]))
        return "Форма отправлена"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1", debug=True)
