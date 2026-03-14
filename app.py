import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/question")
def get_question():
    a = random.randint(2, 12)
    b = random.randint(2, 12)
    return jsonify({"a": a, "b": b, "answer": a * b})
