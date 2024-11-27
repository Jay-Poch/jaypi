from flask import jsonify, request, Blueprint
import random
import sqlite3
random_message = Blueprint("random_message", __name__ )
@random_message.route("/user/message/<name>")
def message(name):
    conn = sqlite3.connect("message.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    message TEXT NOT NULL
)""")
    message = request.args.get("message")
    return_json = False #on default it should return a string
    if request.args.get("return_json"): #if someone set the return_json flag and its true it should return json data
        if request.args.get("return_json") == "True": #true is a string beacuse request.args.get("return_json") only returns strings
            return_json = True
    cursor.execute("""INSERT INTO users (name, message)
                  VALUES (?, ?)""", (name, message))
    cursor.execute("SELECT * FROM users")
    randMessage = cursor.fetchall()
    cursor.execute("""SELECT COUNT(*) FROM users""")
    count = cursor.fetchone()[0]

    randomMassage = randMessage[random.randrange(0, count)] # select the entry for the random massege
    if return_json == False:
        randMessage = randomMassage[2] + " - " + randomMassage[1]
    else:
        randMessage = {randMessage[2]: randMessage[1]}
        randMessage = jsonify(randMessage)
    #print(randomMassage)   #debug
    conn.commit()
    conn.close()
    return randMessage 
