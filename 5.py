import subprocess
import chardet

args_1 = ['ping', '-n', '4', 'yandex.ru']
ya_ping_1 = subprocess.Popen(args_1, stdout=subprocess.PIPE)
for line in ya_ping_1.stdout:
    result = chardet.detect(line)
    #print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

args_2 = ['ping','-n', '4', 'youtube.com']
ya_ping_2 = subprocess.Popen(args_2, stdout=subprocess.PIPE)
for line in ya_ping_2.stdout:
    result = chardet.detect(line)
    #print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
