# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "I'm is Developer for 1000000$ !"
app.run()