my_list = ['class', 'function', 'method']

for i in my_list:
    w = eval(f'b"{i}"')
    print(f' {w} тип данных: {type(w)} длина: {len(w)}')