'''

Создать простое Python-приложение для моделирования покупок в интернет-магазине.
Программа должна рассчитывать общую стоимость товаров с учетом скидок,
управлять корзиной покупок и складскими запасами, а также демонстрировать основные возможности
 Python: работу со строками, числами, списками, словарями, кортежами и множествами.

'''



# 1. Строки и числа

product_name = "Laptop"  # строка

price = 1500.99  # дробное число

discount = 0.10  # дробное число (скидка 10%)



# 2. Индексация строк

first_letter = product_name[0]  # Получаем первую букву строки

print(f"Первый символ названия продукта: {first_letter}\n")



# 3. Динамическая типизация

quantity = 2  # целое число, можно изменять

total_cost = price * quantity  # Python автоматически определяет тип данных

print(f"Стоимость без скидки: {total_cost} $")



# 4. Операторы and и or

has_discount = True

is_member = False

final_price = total_cost

if has_discount and not is_member:

    final_price = round(total_cost - (total_cost * discount), 2)



print(f"Стоимость со скидкой: {final_price} $")



# 5. Методы строк

upper_product_name = product_name.upper()  # Перевод строки в верхний регистр

print(f"Название продукта в верхнем регистре: {upper_product_name}")



# 6. Списки

cart = ["Laptop", "Mouse", "Keyboard"]  # список товаров в корзине

cart.append("USB Cable")  # добавление товара в корзину

print(f"Корзина: {cart}")



# Удаление элемента с помощью метода pop

removed_item = cart.pop(1)  # Удаляет и возвращает элемент по индексу 1 (второй элемент)

print(f"Удаленный товар из корзины: {removed_item}")

print(f"Корзина после удаления: {cart}")



# 7. Словари

inventory = {

    "Laptop": 10,

    "Mouse": 50,

    "Keyboard": 30,

    "USB Cable": 20

}  # словарь с количеством товаров на складе



# Проверка наличия товара

item_to_check = "Mouse"

print(f"В наличии {inventory[item_to_check]} {item_to_check}(ов)")



# Удаление элемента из словаря с помощью del

del inventory["Keyboard"]  # Удаляем элемент с ключом "Keyboard"

print(f"Инвентарь после удаления: {inventory}")



# 8. Изменяемые и неизменяемые объекты

# Списки - изменяемые

cart[0] = "Gaming Laptop"

print(f"Обновленная корзина: {cart}")



# Строки - неизменяемые

try:

    product_name[0] = "T"  # Это вызовет ошибку, так как строки неизменяемы

except TypeError as e:

    print(f"Ошибка: {e}")



# 9. Кортежи

# Кортежи неизменяемы

order_details = ("Order123", 1500.0, "Processing")  # кортеж с данными заказа

print(f"Детали заказа: {order_details}")



# 10. Множества

# Множество хранит уникальные значения

unique_items = {"Laptop", "Mouse", "Keyboard", "Mouse"}  # дублирующийся элемент будет проигнорирован

print(f"Уникальные товары в корзине: {unique_items}")



# Итог

print(f"Итоговая стоимость заказа: {final_price} $")