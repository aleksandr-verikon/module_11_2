

def introspection_info(obj):
    object_type = type(obj) #Тип
    attributes = dir(obj) #Атрибуты объекта
    methods = [attr for attr in attributes if callable(getattr(obj, attr))] #Методы объекта
    module_name = getattr(obj, '__module__', 'Ошибочка получилась' if isinstance(obj, (int, float, complex, str, list, dict, set, tuple)) else None)

    info = {'type': object_type,
    'attributes': attributes,
    'methods': methods,
    'module': module_name,}
    return info




number_info = introspection_info(24)
print(number_info)