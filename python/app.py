import flask

_PORT = 3000

app = flask.Flask(__name__)


@app.route("/greeting")
def greet():
    who = flask.request.args.get("name", "world")
    return f"Hello {who}"


if __name__ == "__main__":
    app.run(port=_PORT)
