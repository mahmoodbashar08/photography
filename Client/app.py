from flask_mysqldb import MySQL
import sys
sys.path.append('..')
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
mysql = MySQL(app)

@app.route("/<name>")
def index(name):
    return render_template('/index.html', var=name)


@app.route("/photo/1")
def display():
    cur = mysql.connection('photography.db')
    cur.execute('SELECT * FROM photos')
    rv = cur.fetchall()
    return str(rv)

if __name__ == "__main":
    app.run()
