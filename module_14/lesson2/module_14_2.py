import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{i*10}", "1000"))

for i in range(1, 11, 2):
    cursor.execute(f"UPDATE Users SET balance = ? WHERE id = ?", (500, i))

for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (i, ))

cursor.execute("SELECT * FROM Users WHERE age != ?", (60,))
'''
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}")
'''
cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total1 = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
total2 = cursor.fetchone()[0]
print(total2/total1)
connection.commit()
connection.close()