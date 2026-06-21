from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


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
