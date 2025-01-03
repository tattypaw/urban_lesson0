import sqlite3

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email NEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')
    connection.commit()

def get_all_products():
    con = sqlite3.connect("products.db")
    curs = con.cursor()
    products = curs.execute("SELECT * FROM Products")
    '''for product in products:
        print(f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}")'''
    return products

def add_user(username, email, age):
    conn = sqlite3.connect("products.db", timeout=7)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (username, email, age, 1000))
    conn.commit()
    conn.close()

def is_included(username):
    connec = sqlite3.connect("products.db")
    cur = connec.cursor()
    check_user = cur.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check_user.fetchone() is None:
        connec.close()
        return False
    else:
        connec.close()
        return True


connection = sqlite3.connect("products.db")
cursor = connection.cursor()
'''initiate_db()
check = is_included('Lena')
if not check:
    add_user('Lena', 'lena@mail.com', 20)
for i in range(1, 5):
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f"Продукт{i}", f"Описание{i}", f"{i*100}"))
'''
connection.commit()
connection.close()


