import sqlite3

con = sqlite3.connect("photography.db")
cur = con.cursor()

def add_values(file_name, file_download_id, file_path, owner_id): # this function to add values to the database
    con = sqlite3.connect("photography.db")
    cur = con.cursor()
    cur.execute(
        f"INSERT INTO photos(file_name, file_download_id, file_path, owner_id) VALUES ('{file_name}', '{file_download_id}', '{file_path}', {owner_id})")
    con.commit()
    cur.close()
    con.close()


def get_values(file_download_id):  # this function to get values from the database and send it to the bot 
    con = sqlite3.connect("photography.db")
    cur = con.cursor()
    cur.execute(
        f"SELECT * from photos Where file_download_id = '{file_download_id}'")
    con.commit()
    cur.close()
    con.close()

cur.close()
con.close()
