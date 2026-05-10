# app.py
from flask import Flask, request, jsonify
from logic import validate_book

app = Flask(__name__)

# In-memory data store
books = []


@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    # Use our logic layer to validate the data
    if validate_book(data):
        books.append(data)
        return jsonify({"message": "Book added successfully"}), 201

    # Validation failed
    return jsonify({"error": "Invalid book data"}), 400


if __name__ == "__main__":
    app.run(debug=True)
