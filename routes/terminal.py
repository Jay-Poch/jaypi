from flask import Blueprint, jsonify
terminal_blueprint = Blueprint("terminal", __name__)
@terminal_blueprint.route("/terminal/<command>")
def terminal(command):
    match command:
        case "ls":
            testy = {"result": "main.py"}
        case "whoami":
            testy = {"result": "Im a boy that likes coding and cubing and i dont know what to write here yes"}
        case _:
            testy = {"result": "not implemented"}
    return jsonify(testy), 200 
