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

    cursor.execute("""INSERT INTO users (name, message)
                  VALUES (?, ?)""", (name, message))
    cursor.execute("SELECT * FROM users")
    randMessage = cursor.fetchall()
    cursor.execute("""SELECT COUNT(*) FROM users""")
    count = cursor.fetchone()[0]
    #print(count)
    randomMassage = randMessage[random.randrange(0, count)] # the entry for the random massege
    randMessage = randomMassage[2] + " - " + randMessage[random.randrange(0, count)][1]
    #print(randMessage)
    conn.commit()
    conn.close()
    return randMessage 
