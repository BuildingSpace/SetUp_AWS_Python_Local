from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/ping/<user_name>')
def ping(user_name):
    response = user_name + ' just pinged me!'
    return response


if __name__ == '__main__':
    app.run(debug=True)
