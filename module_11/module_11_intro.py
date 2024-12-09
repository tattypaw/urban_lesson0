def introspection_info(obj):
    # Определение типа объекта
    obj_type = type(obj).__name__
    # Получение атрибутов и методов объекта
    attributes_and_methods = dir(obj)
    # Получение атрибутов объекта
    attributes = [attribute for attribute in attributes_and_methods if not callable(getattr(obj, attribute))]
    # Получение методов объекта
    methods = [method for method in attributes_and_methods if callable(getattr(obj, method))]
    # Определение модуля, к которому объект принадлежит
    module = obj.__class__.__module__
    # Создание словаря с информацией об объекте
    info = {
        'type': obj_type, 
        'attributes': attributes, 
        'methods': methods, 
        'module': module}
    return info

number_info = introspection_info(42.45)
print(number_info)
