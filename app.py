from flask import Flask, render_template, request
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
    finalResult = rows[3]
    print("last", finalResult)
    return render_template("index.html", image_loc= finalResult)
    

if __name__ == "__main__":
    app.run()

