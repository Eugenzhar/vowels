# save this as app.py
from flask import Flask
from flask import render_template
from vsearch import search4letters

app = Flask(__name__)

@app.route("/")
def hello():
    return "I'm is Developer for 1000000$ !"

@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the univers, and everything', 'eiru,!'))

@app.route("/entry")
def entry_page() ->'html':
    return render_template('entry.html', the_title='Welcome to search for letters on the web!')

app.run()