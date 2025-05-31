import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def greet():
    return ('<h1 style="text-align: left">Guess a number between 0 and 9!</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=400>')


rand_num = random.randint(0, 9)
print(rand_num)


@app.route("/<int:user_guess>")
def guess_num(user_guess):
    high_guess_url = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
    low_guess_url = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
    correct_guess_url = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

    if user_guess > rand_num:
        return (f'<h1 style="color: purple">Too high, try again!</h1>'
                f'<img src={high_guess_url} width=400>')
    elif user_guess < rand_num:
        return (f'<h1 style="color: red">Too low, try again!</h1>'
                f'<img src={low_guess_url} width=400>')
    else:
        return (f'<h1 style="color: green">You found me!</h1>'
                f'<img src={correct_guess_url} width=400>')


if __name__ == "__main__":
    app.run(debug=True)
