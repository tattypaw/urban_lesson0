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
    connection.commit()

def get_all_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    products = cursor.execute("SELECT * FROM Products")
    '''for product in products:
        print(f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}")'''
    return products


connection = sqlite3.connect("products.db")
cursor = connection.cursor()
initiate_db()

'''for i in range(1, 5):
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f"Продукт{i}", f"Описание{i}", f"{i*100}"))
connection.commit()'''

print(*get_all_products())
connection.close()


