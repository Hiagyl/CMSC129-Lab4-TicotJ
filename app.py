from flask import Flask, request, jsonify, render_template
from logic import validate_book

app = Flask(__name__)

db = {
    "books": []
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not validate_book(data):
        return jsonify({"error": "Invalid book data", "status": "fail"}), 400

    new_book = {
        "title": data["title"].strip(),
        "author": data["author"].strip()
    }
    db["books"].append(new_book)
    return jsonify({"message": "Book added successfully", "status": "success"}), 201


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": db["books"]}), 200


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if 0 <= book_id < len(db["books"]):
        db["books"].pop(book_id)
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "fail"}), 404


@app.route('/books/<int:book_id>', methods=['PUT'])
def edit_book(book_id):
    data = request.get_json()
    if 0 <= book_id < len(db["books"]) and validate_book(data):
        db["books"][book_id] = data
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "fail"}), 400


if __name__ == "__main__":
    app.run(debug=True)
