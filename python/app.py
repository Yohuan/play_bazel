import flask

_HOST = "0.0.0.0"
_PORT = 3000

app = flask.Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host=_HOST, port=_PORT)
