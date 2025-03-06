from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index0():
    return render_template("index.html", username="Иванов", title="Миссия колонизации Марса")


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == "GET":
        return render_template("registration.html")
    elif request.method == "POST":
        man = dict()
        man["email"] = request.form.get("email")
        man["school_class"] = request.form.get("class")
        man["about"] = request.form.get("about")

        return render_template("auto_answer.html", **man)


list_profession = ["капитан", "пилот", "строитель", "врач"]


@app.route('/list_prof/<num>')
def list_prof(num):
    return render_template("list_prof.html", list_prof=list_profession, op=num)


@app.route('/index')
def index():
    return "И на марсе будут яблони цвести!"


@app.route('/astronaut_selection')
def astronaut_selection():
    with open("templates/ttt.txt", encoding="utf-8") as file:
        return file.read()

    return render_template('index.html')


@app.route('/promotion')
def promotion():
    return "Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!"


@app.route('/image_mars')
def image_mars():
    return '''<html><title>Привет, Марс!</title><h1>Жди нас, Марс!</h1><img src="static/Images/mars.png" alt="Mars surface" width=500 height=500><br><br>Вот она красная планета!</html>'''


@app.route('/promotion_image')
def promotion_image():
    return '''<!DOCTYPE html>
<html lang="ru">
<head>
    <title>Колонизация</title>
    <link rel="stylesheet" href="static/css/style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>

<body>
<h1 class="welcome_text">Жди нас марс!</h1>
<img src="static/Images/mars.png" alt="Mars surface" width=500 height=500>
<div class="p-3 mb-2 bg-primary text-white">Человечество вырастает из детства.</div>
<div class="p-3 mb-2 bg-secondary text-white">Человечеству мала одна планета.</div>
<div class="p-3 mb-2 bg-danger text-white">Мы сделаем безжизнеными пока планеты.</div>
<div class="p-3 mb-2 bg-warning text-white">И начнём с Марса!</div>
<div class="p-3 mb-2 bg-info text-white">Присоединяйся!</divЮ
</body>

</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
