import flask
from flask import render_template
from flask import request
from flask import redirect


app: flask.Flask = flask.Flask(__name__)


def main() -> None:
    global app

    APP_ADDRESS: str = "localhost"
    APP_PORT: int = 8000

    app.run(host=APP_ADDRESS, port=APP_PORT, debug=True)


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    if request.method == "POST":
        pass

    return render_template("index.html")


if __name__ == "__main__":
    main()
