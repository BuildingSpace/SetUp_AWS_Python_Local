from flask import Flask
from math import sqrt

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/ping/<user_name>')
def ping(user_name):
    response = user_name + ' just pinged me!'
    return response

@app.route('/encodingStuff/<string_to_be_decoded>')
def encodingStuff(string_to_be_decoded):
    UTF8_encoding = {'encoding': '%21', 'character': '!'}
    if UTF8_encoding.get('character') == string_to_be_decoded:
        return 'Decoded Value is : '+ UTF8_encoding.get('encoding')
    else:
        return 'Code not available'

@app.route('/isItPrime/<number>')
def isItPrime(number):
    try:
        val = int(number)
        return val
    except ValueError:
        answer = "That's indian bread!"
        return answer

if __name__ == '__main__':
    app.run(debug=True)
