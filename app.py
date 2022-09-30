from flask import Flask, render_template, send_file
import sqlite3


app = Flask(__name__)


@app.route("/photos/<string:file_download_id>")
def hello_world(file_download_id):
    conn = sqlite3.connect('photography.db')
    posts = conn.execute(
        f"SELECT * FROM photos WHERE file_download_id ='{file_download_id}'").fetchall()
    for rows in posts:
        print("final", rows)
    conn.close()
    myString = rows[2]
    finalResult = rows[3]
    print("last", finalResult)
    return render_template("index.html", image_loc=finalResult, myString=myString)
    

@app.route("/photos/<string:file_download_id>/download_file")
def download_this_file(file_download_id):
    conn = sqlite3.connect('photography.db')
    posts = conn.execute(
        f"SELECT * FROM photos WHERE file_download_id ='{file_download_id}'").fetchall()
    for rows in posts:
        print("final", rows)
    conn.close()
    finalResult = rows[3]
    return send_file( "static/" + finalResult,as_attachment=True)

if __name__ == "__main__":
    app.run()

