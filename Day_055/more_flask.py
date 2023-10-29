from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bold():
        return f"<b>{function()}</b>"

    return bold


def make_emphasis(function):
    def emphasis():
        return f"<em>{function()}</em>"

    return emphasis


def make_underlined(function):
    def underlined():
        return f"<u>{function()}</u>"

    return underlined

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


# @app.route("/")
# def hello_world():
#     return "<h1>Hello, World!</h1>"

@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a new paragraph.</p>'
            '<img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" width=400>')


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


# @app.route("/username/<name>/1")
# def greet(name):
#     return f"Hello there {name}"

# @app.route("/username/<path:name>")
# def greet(name):
#     return f"Hello there {name}"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old."


if __name__ == "__main__":
    app.run(debug=True)
