my_list = ['attribute', 'класс', 'функция', 'type', 'fffыы']
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        if ord(my_list[i][j]) > 127:
            print(f'Слово {my_list[i]} невозможно записать в байтовом типе.')
            break
        