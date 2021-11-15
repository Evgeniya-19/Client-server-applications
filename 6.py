import locale

my_list = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as f_n:
    for line in my_list:
        f_n.write(line + '\n')

print(f_n)
file_coding = locale.getpreferredencoding()


with open('test_file.txt', 'r', encoding=file_coding) as f_n:
    for i in f_n:
        print(i)



