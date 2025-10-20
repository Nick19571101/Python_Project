import os
path, path1, path2, src, dst = None
# Создание, удаление, переход
os.mkdir(path)  # создать одну директорию
os.makedirs(path)  # создать директорию и все промежуточные
os.rmdir(path)  # удалить пустую директорию
os.removedirs(path)  # удалить директорию и все пустые родительские
os.chdir(path)  # сменить текущую рабочую директорию
os.getcwd()  # получить текущую рабочую директорию
# Список файлов и каталогов
os.listdir(path)  # список содержимого директории
os.scandir(path)  # итерируемый объект с метаданными (эффективнее чем listdir)
os.walk(path)  # генератор обхода дерева директорий
#Удаление и перемещение файлов
os.remove(path)  # удалить файл
os.rename(src, dst)  # переименовать файл или переместить
os.replace(src, dst)  # как rename, но перезаписывает
os.unlink(path)  # синоним remove (удаление файла)
#os.path — работа с путями
# Объединение и получение компонентов
os.path.join()  # объединить части пути
os.path.basename(path)  # имя файла
os.path.dirname(path)  # директория файла
os.path.split(path)  # кортеж (dirname, basename)
os.path.splitext(path)  # кортеж (name, ext)
#Проверка существования и типа
os.path.exists(path)  # существует ли путь
os.path.isfile(path)  # является ли файлом
os.path.isdir(path)  # является ли директорией
os.path.islink(path)  # является ли симлинком
#Прочее
os.path.getsize(path)  # размер файла в байтах
os.path.abspath(path)  # абсолютный путь
os.path.normpath(path)  # нормализованный путь (убирает .., .)
os.path.realpath(path)  # реальный путь (с учётом симлинков)
os.path.samefile(path1, path2)  # указывают ли два пути на один и тот же файл