my_list = ['разработка', 'сокет', 'декоратор']
my_list_code = [b'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                b'\u0441\u043e\u043a\u0435\u0442]',
                b'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

for i in range(len(my_list)):
    print(f' {my_list[i]} {type(my_list[i])}')
    print(f' {my_list_code[i]} {type(my_list_code[i])}')


