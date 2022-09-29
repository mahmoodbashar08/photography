from flask import Flask, render_template, request, send_file
import sqlite3


app = Flask(__name__)

# conn = sqlite3.connect('photography.db')
# posts = conn.execute('SELECT * FROM photos ').fetchall()
# conn.close()
# for rows in posts:
#     print(rows)


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
    myString = rows[2]
    finalResult = rows[3]
    return send_file( "static/" + finalResult,as_attachment=True)

if __name__ == "__main__":
    app.run()

