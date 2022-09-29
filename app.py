# from calendar import c
# from cgitb import reset
# from flask import Flask, render_template, request
# import sqlite3


# app = Flask(__name__)

# # conn = sqlite3.connect('photography.db')
# # posts = conn.execute('SELECT * FROM photos ').fetchall()
# # conn.close()
# # for rows in posts:
# #     print(rows)


# @app.route("/photos/<string:file_download_id>")
# def hello_world(file_download_id):
#     conn = sqlite3.connect('photography.db')
#     posts = conn.execute(
#         'SELECT * FROM photos WHERE file_download_id = "Uyi2JM" ').fetchall()
#     for rows in posts:
#         print("final", rows)
#     conn.close()
#     finalResult = rows[3]
#     print("last", finalResult)
#     return render_template("index.html")
    

# if __name__ == "__main__":
#     app.run()


from flask import Flask, render_template, redirect, url_for, request
# Route for handling the login page logic
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
#within app.route add the html page we are doing changes to


@app.route('/register')
# def is normally how we define a function in python
def register():
 return render_template('register.html')


@app.route('/registerV')
def registerV():
 return render_template('registerV.html')
