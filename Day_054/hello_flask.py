from flask import Flask
from simple_dotenv import GetEnv
# from dotenv import load_dotenv


env = GetEnv('ENV_VARIABLE_KEY')


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
