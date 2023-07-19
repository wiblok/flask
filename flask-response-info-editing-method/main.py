from flask import Flask, jsonify, make_response, redirect

app = Flask(__name__)

@app.route("/json")
def json_response():
    # JSONレスポンスの生成
    return jsonify({"message": "This is a JSON response"})

@app.route("/html")
def html_response():
    # HTMLレスポンスの生成
    response = make_response("<h1>This is an HTML response</h1>")
    return response

@app.route("/custom-header")
def custom_header_response():
    # レスポンスヘッダーの設定
    response = make_response("This response has a custom header")
    response.headers["Custom-Header"] = "Custom Value"
    return response

@app.route("/status-code")
def status_code_response():
    # ステータスコードの設定
    response = make_response("Created", 201)
    return response

@app.route("/redirect")
def redirect_response():
    # リダイレクトの実行
    return redirect("/json")

@app.route("/error")
def error_response():
    # エラーレスポンスの生成
    response = make_response(jsonify({"error": "An error occurred"}), 500)
    return response