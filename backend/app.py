from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Home API
@app.route("/")
def home():
    return "Ranjitha Portfolio Backend Running"


# Contact Form API
@app.route("/contact", methods=["POST"])
def contact():

    data = request.json

    name = data["name"]
    email = data["email"]
    message = data["message"]


    conn = sqlite3.connect("portfolio.db")

    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO messages(name,email,message)
    VALUES(?,?,?)
    """,
    (name,email,message))


    conn.commit()
    conn.close()


    return jsonify(
        {
            "message":"Message submitted successfully"
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
