from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_graph():
    data = request.get_json()
    selected_graph = data["graph"]

    # Execute the graphGenerator.py with the selected graph
    subprocess.run(["python", "graphGenerator.py", selected_graph])

    return jsonify({"message": "Graph generated successfully"})


if __name__ == "__main__":
    app.run()
