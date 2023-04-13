import os
from pathlib import Path

# функцию создания нового файла (create).
def create(name):
    if os.path.exists(name):
    # if name in os.listdir():
        print( 'Такой файл уже существует!')
        return False
    else:
        open(name, 'w+')
        print(f'Файл {name} успешно создан')
        return name



# функцию вывода списка файлов и директорий (list).
def list():
    files = os.listdir()
    # добавляем к названию директории "/", для удобства просмотра
    for i in range(len(files)):
        if os.path.isdir(files[i]):
            files[i] += '/'
    print(files)
    return  files


# функцию копирования файла (copy).
def copy(src, dst = None):
    same_files = []
    # если аргумент dst передан, сопоставляем его с другими файлами на одинаковые названия
    if dst is not None:
        if dst in os.listdir():
            dst = input('Файл с таким названием уже существует, введите другое название:')
        Path(dst).write_bytes(Path(src).read_bytes())
    # если аргумент не передан то копируем файл с исконным называние файла + "копия_число"
    else:
        pre_dst = src.split('.')[0]+'_копия_'
        for i in os.listdir(): # проверяем на совпадение части названий других файлов
            if os.path.isfile(i):
                if pre_dst in i:
                  same_files.append(i.split('.')[0]) # список из файлов с частично одинаковыми названиями
        numbers = []
        if same_files:
            for i in same_files:
                try:
                    numbers.append(int(i[len(pre_dst):])) # пытаемя получить цифру после частичного названия
                except:
                    continue
        if numbers:
            dst = pre_dst + str(max(numbers) + 1) + '.' +  src.split('.')[-1] # вытаскиваем максимально число после чатичного названия файлов и создаем новый файл с названием и цифрой большей на 1
        else:
            dst = pre_dst + '1' + '.' +  src.split('.')[-1] # если таковых нет, то создаем файл с название "файл_копия_1.расширение"
        Path(dst).write_bytes(Path(src).read_bytes())
    return dst


# функцию перемещения файла (move).
def move(src, dst = None):
    file_name = src.split('/')[-1] # название файла в src
    if dst and dst != ' ':
        directory = dst.split('/')
        # проверка на наличие названия файла в dst
        if '.' not in  directory[-1] or directory[-1] == '':
            directory = '/'.join(directory)
            if directory[-1] != '/':
                directory += '/'
        else:
            file_name = directory[-1] # название файла в dst
            directory[-1] = '' # оставляем только последовательность дирректорий
            directory = '/'.join(directory)
        # проверка на существования диреектории
        if os.path.exists(directory):
            os.rename(src, (directory + file_name))
        else:
            while not os.path.exists(directory):
                directory = input('Указанной директории не существует, попробуйте снова:')
            os.rename(src, (directory + file_name))
    # если dst не указан или равен " ", то перемещаем его в директорию где запускается скрипт
    else:
        directory = os.path.abspath(os.curdir) + '/'
        os.rename(src, (directory + file_name))


# функцию инициализации новой файловой системы (init).
def init(directories):
    while os.path.exists(directories):
        directories = input('Такая файловая система уже существует, введите другую:')
    os.makedirs(directories)




# create('hello.txt')
# list()
# copy('hello.txt')
# move('test/test_2/hello_копия_2.txt','')
# move('hello_копия_3.txt', 'test/test_2/index.txt')
# init('file/file1/file3')
