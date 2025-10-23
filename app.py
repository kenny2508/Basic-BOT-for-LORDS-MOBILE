from flask import Flask, jsonify, request
from core.engine import GameEngine

app = Flask(__name__)
engine = GameEngine()

@app.route("/")
def home():
    return jsonify({"message": "Lords Mobile Bot API running!"})

@app.route("/shield/<user_id>")
def shield_status(user_id):
    return jsonify({"status": engine.check_shield(user_id)})

@app.route("/shield/renew/<user_id>", methods=["POST"])
def renew_shield(user_id):
    return jsonify({"result": engine.renew_shield(user_id)})

@app.route("/resources/<user_id>")
def resources(user_id):
    return jsonify({"data": engine.get_resources(user_id)})

@app.route("/gather", methods=["POST"])
def gather():
    data = request.json
    return jsonify({
        "result": engine.gather_resources(data["user_id"], data["type"], data["amount"])
    })

@app.route("/guild/join", methods=["POST"])
def join_guild():
    data = request.json
    return jsonify({"result": engine.join_guild(data["user_id"], data["guild_id"])})

@app.route("/hunt", methods=["POST"])
def hunt():
    data = request.json
    return jsonify({"result": engine.hunt_monster(data["user_id"], data["monster_level"])})

@app.route("/rally", methods=["POST"])
def rally():
    data = request.json
    return jsonify({"result": engine.join_rally(data["user_id"], data["rally_id"])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
