import os
from pathlib import Path

# функцию создания нового файла (create).
def create(name):
    if os.path.exists(name):
    # if name in os.listdir():
        print( 'Такой файл уже существует!')
    else:
        open(name, 'w+')
        print(f'Файл {name} успешно создан')



# функцию вывода списка файлов и директорий (list).
def list():
    files = os.listdir()
    # добавляем к названию директории "/", для удобства просмотра
    for i in range(len(files)):
        if os.path.isdir(files[i]):
            files[i] += '/'
    return  files


# функцию копирования файла (copy).
def copy(src, dst = None):
    same_files = []
    if dst is not None:
        if dst in os.listdir():
            dst = input('Файл с таким названием уже существует, введите другое название:')
        Path(dst).write_bytes(Path(src).read_bytes())
    else:
        pre_dst = src.split('.')[0]+'_копия_'
        for i in os.listdir():
            if os.path.isfile(i):
                if pre_dst in i:
                  same_files.append(i.split('.')[0])
        numbers = []
        if same_files:
            for i in same_files:
                try:
                    numbers.append(int(i[len(pre_dst):]))
                except:
                    continue
        if numbers:
            dst = pre_dst + str(max(numbers) + 1) + '.' +  src.split('.')[-1]
        else:
            dst = pre_dst + '1' + '.' +  src.split('.')[-1]
        Path(dst).write_bytes(Path(src).read_bytes())







create('hello.txt')
print(list())
copy('hello.txt')
