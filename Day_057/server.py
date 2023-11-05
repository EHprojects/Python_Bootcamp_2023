from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


def get_age(name):
    params = {
        "name": name,
    }

    age_response = requests.get(url="https://api.agify.io", params=params)
    age_response.raise_for_status()

    age_guess = age_response.json()["age"]
    return age_guess


def get_gender(name):
    params = {
        "name": name,
    }

    gender_response = requests.get(url="https://api.genderize.io", params=params)
    gender_response.raise_for_status()

    gender_guess = gender_response.json()["gender"]
    return gender_guess


@app.route("/")
def home():
    rand_num = random.randint(1, 10)
    current_year = datetime.now().year
    my_name = "EH Projects"
    return render_template("index.html", num=rand_num, year=current_year, name=my_name)


# Day 33 for API requests
@app.route("/guess/<name>")
def guess(name):
    name = str(name).title()
    age = get_age(name)
    gender = get_gender(name)
    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
