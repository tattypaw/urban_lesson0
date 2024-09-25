def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
        return
    inner_function()
    return

test_function()
# inner_function() - NameError: name 'inner_function' is not defined
# функция не видна в пространстве глобальных имен