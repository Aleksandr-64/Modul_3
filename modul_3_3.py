print(),print('Задание 1:')
def print_params(a = 1, b = 'строка', c = True): #1
    print(a, b, c)

print_params()
print_params('Vasya','Petya','Dimon')
print_params(4,'Books')
print_params(b = 25)
print_params(c = [1, 2, 3])

print(),print('Задание 2:')

#2
values_list = 3, 'soft', False
values_dict = {'a': 2, 'b': 'Хорошо', 'c': (3,5,6)}

print_params(*values_list)
print_params(**values_dict)

print(),print('Задание 3:')

#3
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)