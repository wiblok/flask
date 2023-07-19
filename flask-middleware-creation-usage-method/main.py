from flask import Flask

app = Flask(__name__)

class Middleware():
    def __init__(self, app):
        self.wrapped_app = app

    def __call__(self, environ, start_response):
        print('ミドルウェアの実行')
        return self.wrapped_app(environ, start_response)

app.wsgi_app = Middleware(app.wsgi_app)

@app.route('/')
def root():
    return {"message": "Hello, World!"}