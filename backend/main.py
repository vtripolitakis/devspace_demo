from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def root():
    return "OK", 200


@app.route("/hello")
def hello():
    return jsonify({"hello": "world"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
