# save this as app.py
from flask import Flask
from vsearch import search4letters
app = Flask(__name__)

@app.route("/")
def hello():
    return "I'm is Developer for 1000000$ !"

@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the univers, and everything', 'eiru,!'))
app.run()