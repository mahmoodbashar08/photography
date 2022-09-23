import sqlite3


# INSERT INTO photos(file_name, file_path, file_download_id, owner_id, is_deleted) VALUES ("F.jpeg", "/uploads/me.jpeg", 12, 01, false)
con = sqlite3.connect("photography.db")
cur = con.cursor()


# def add_values():
cur.execute("INSERT INTO photos(file_name, file_download_id, file_path, owner_id, is_deleted) VALUES ('FL.jpeg', '/uploads/me.jpeg', 16, 10, false)")


# add_values()

cur.execute("SELECT * FROM photos")
rows = cur.fetchall()
for row in rows:
    print(row)
