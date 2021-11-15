my_list = ['разработка', 'администрирование', 'protocol', 'standard']
my_list_bytes = []
my_list_2 = []
for i in range(len(my_list)):
    my_list_bytes.append(my_list[i].encode('utf-8'))
    print(my_list_bytes[i])

for i in range(len(my_list_bytes)):
    my_list_2.append(my_list_bytes[i].decode('utf-8'))
    print(my_list_2[i])
