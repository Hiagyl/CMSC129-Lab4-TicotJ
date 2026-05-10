# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# No routes defined yet = 404 errors for our tests

if __name__ == "__main__":
    app.run(debug=True)
