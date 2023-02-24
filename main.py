# Flask
from flask import (
    Flask, 
    render_template,
)
from flask.app import Flask as FlaskApp


app: FlaskApp = Flask(__name__)

@app.route("/")
def main_page() -> str:
    return 'CALCULATOR'

@app.route('/<int:num1>/<int:num2>/<id3>')
def article(num1: int, num2: int, id3: str):
    try:
        if id3 == "+":
            return f'{num1} + {num2} = {num1 + num2}'
        elif id3 == "-":
            return f'{num1} - {num2} = {num1 - num2}'
        elif id3 == "*":
            return f'{num1} * {num2} = {num1 * num2}'
        elif id3 == "--":
            return f'{num1} / {num2} = {num1 / num2}'
        elif id3 == "%":
            return f'{num1} % {num2} = {num1 % num2}'
        else:
            return 'wrong'
    except:
        return "No zero"

if __name__ == '__main__':
    app.run(
        port=8080,
        debug=True
    )