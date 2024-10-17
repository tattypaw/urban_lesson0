import os

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        s = self.name + ', ' + str(self.weight) + ', ' + self.category
        return s

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        if os.path.exists(self.__file_name):
            file = open(self.__file_name, 'r')
            products = file.read()
            file.close()
            return products
        else:
            return ''

    def add(self, *products):
        products_in_shop = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if str(product) in products_in_shop:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(str(product)+'\n')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())