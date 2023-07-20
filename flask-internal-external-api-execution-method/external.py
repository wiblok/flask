from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/data')
def get_data():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"message": "Error occurred"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)