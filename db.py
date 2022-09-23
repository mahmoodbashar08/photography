import sqlite3


# INSERT INTO photos(file_name, file_path, file_download_id, owner_id, is_deleted) VALUES ("F.jpeg", "/uploads/me.jpeg", 12, 01, false)
con = sqlite3.connect("photography.db")
cur = con.cursor()


def add_values(file_name, file_download_id, file_path, owner_id):
    con = sqlite3.connect("photography.db")
    cur = con.cursor()
    cur.execute(
        f"INSERT INTO photos(file_name, file_download_id, file_path, owner_id) VALUES ('{file_name}', '{file_download_id}', '{file_path}', {owner_id})")
    con.commit()
    cur.close()
    con.close()

# add_values("hello", "hi", "aaa", 12)


cur.execute("SELECT * FROM photos")
rows = cur.fetchall()
for row in rows:
    print(row)
# cur.close()
# con.close()
