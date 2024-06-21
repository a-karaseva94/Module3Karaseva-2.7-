def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# 1.Функция с параметрами по умолчанию:
print_params()
# print_params(a, b, c) не работает, потому что при этом написании в функции с параметрами по умолчанию нужно их задать
# print_params(a, c) не работает, потому что сколько параметров определено, столько и должно быть вызвано
print_params(b = 25)
print_params(c = [1,2,3])

# 2.Распаковка параметров:
values_list = [7, True, 'Anastasiia']
values_dict = {'a': 55, 'b': 'Karaseva', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# 3. Распаковка + отдельные параметры:
values_list_2 = ['hi', 9]
print_params(*values_list_2, 42)