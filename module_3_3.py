def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [5, 'string', False]
values_dict = {'a': 17, 'b': True, 'c': 'text'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 26]
print_params(*values_list_2, 42)
print_params()