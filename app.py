# app.py
from flask import Flask, request, jsonify
from logic import validate_book

app = Flask(__name__)

# REFACTOR: Using a structured dictionary to represent our "Database"
# This makes it easier to expand to multiple collections later.
db = {
    "books": []
}


@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    if not validate_book(data):
        return jsonify({"error": "Invalid book data", "status": "fail"}), 400

    # REFACTOR: Clean the data before saving (strip whitespace)
    new_book = {
        "title": data["title"].strip(),
        "author": data["author"].strip()
    }

    db["books"].append(new_book)
    return jsonify({"message": "Book added successfully", "status": "success"}), 201


@app.route('/books', methods=['GET'])
def get_books():
    """Added a GET route to verify the integration works both ways"""
    return jsonify({"books": db["books"]}), 200


if __name__ == "__main__":
    app.run(debug=True)
