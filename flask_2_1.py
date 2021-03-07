from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm


app = Flask(__name__)

@app.route('/', defaults={'title_web': None})
@app.route('/index/<title_web>')
def index(title_web):
    return render_template('base.html', title=title_web)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')