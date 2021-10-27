# save this as app.py
from flask import Flask
from flask import render_template, request
from vsearch import search4letters

app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req, res, file=log)


@app.route("/")
def hello():
    return "I'm is Developer for 1000000$ !"

@app.route('/search4', methods=['GET','POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results: '
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase = phrase,
                           the_letters = letters,
                           the_title = title,
                           the_results = results,)

@app.route("/entry")
def entry_page() ->'html':
    return render_template('entry.html', the_title='Welcome to search for letters on the web!')

@app.route("/viewlog")
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return contents
if __name__ == '__main__':
    app.run(debug=True)