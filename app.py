#
#   vsearch4web.py
#   тема из книги О,Рэйли
from flask import Flask
from flask import render_template, request, escape
from vsearch import search4letters
import mysql.connector
app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    dbconfig = {'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB',}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    # with UseDatabase(dbconfig) as cursor:

    _SQL = """insert in to log
    (phrase, letters, ip, browser_string, results)
    values
    (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],
                         req.form['letters'],
                         req.remote_addr,
                         req.user_agent.browser,
                         res,))
    conn.commit()
    cursor.close()
    conn.close()



@app.route("/")
def hello():
    return "I'm is Developer for 1000000$ !"

@app.route('/search4', methods=['GET','POST'])
def do_search() -> 'html':
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
def view_the_log() -> 'HTML':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))    # список списков  [[],[],[]]
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)

    return str(contents)
if __name__ == '__main__':
    app.run(debug=True)