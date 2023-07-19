from flask import Flask, jsonify, request

app = Flask(__name__)

# ユーザー情報を保持する仮のデータ
users = [
    {"id": 1, "name": "John Doe", "uses": 5},
    {"id": 2, "name": "Jane Doe", "uses": 3},
    {"id": 3, "name": "Jim Doe", "uses": 7},
]

@app.route("/users/<int:user_id>", methods=['GET'])
def read_user(user_id):
    # ユーザー情報の取得処理など...
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"message": "User not found"})

@app.route("/users", methods=['GET'])
def read_users():
    return jsonify(users)

@app.route("/users", methods=['POST'])
def create_user():
    # ユーザーの作成処理など...
    user = request.get_json()
    users.append({"id": len(users) + 1, "name": user["name"], "uses": user["uses"]})
    return jsonify(users[-1])

@app.route("/users/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    # ユーザーの更新処理など...
    user = request.get_json()
    for u in users:
        if u["id"] == user_id:
            u["name"] = user["name"]
            u["uses"] = user["uses"]
            return jsonify(u)
    return jsonify({"message": "User not found"})

@app.route("/users/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    # ユーザーの削除処理など...
    for u in users:
        if u["id"] == user_id:
            users.remove(u)
            return jsonify({"message": f"User {user_id} has been deleted."})
    return jsonify({"message": "User not found"})


