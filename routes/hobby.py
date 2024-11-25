from flask import Blueprint, jsonify
import random
hobby_blueprint = Blueprint("hobby", __name__)

@hobby_blueprint.route("/hobby/random")
def home():
    hobby = ["cubing", "coding", "playing videogames", "linux"]
    testy = {"result": hobby[random.randrange(0, 4)]}
    return jsonify(testy), 200 
