from flask import Flask
# from simple_dotenv import GetEnv

# env = GetEnv('ENV_VARIABLE_KEY')


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
