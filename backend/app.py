from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


notes = []


@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "Backend running"})


@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()
    if not data or "note" not in data:
        return jsonify({"error": "Note required"}), 400
    notes.append(data["note"])
    return jsonify({"message": "Note added", "total_notes": len(notes)}), 201


@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify({"notes": notes})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
