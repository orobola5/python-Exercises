from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


@app.route("/get_news")
def get_news():
    return "no news is good news"




if __name__ == '__main__':
    app.run(port=5000, debug=True)
