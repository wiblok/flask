from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/items/", methods=["POST"])
def create_item():
    item = request.json
    user_agent = request.headers.get('User-Agent')
    item.update({"user_agent": user_agent})
    return jsonify(item)