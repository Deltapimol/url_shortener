import uuid
from flask import Flask

app = Flask(__name__)


URL_MAPPINGS = dict()


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()