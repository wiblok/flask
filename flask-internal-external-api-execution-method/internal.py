# モジュールをインポートします
from flask import Flask, request, jsonify
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin  
import os

# Flaskアプリケーションを作成します
app = Flask(__name__, static_url_path='')

CORS(app)

# ユーザーを保存するための仮のデータストア
users = []

@app.route('/')
def root():
    return send_from_directory('', 'templates/index.html')

@app.route('/users', methods=['GET'])
def get_users():
    # ユーザーデータをレスポンスとして返す
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    # リクエストボディからユーザーデータを取得
    user = request.get_json()
    # ユーザーをデータストアに追加
    users.append(user)
    # 新しく作成されたユーザーをレスポンスとして返す
    return jsonify(user), 201

if __name__ == "__main__":
    app.run(port=5000, debug=True)