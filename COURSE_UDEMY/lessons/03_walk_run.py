# from posixpath import islink
import subprocess
import time
import os

ways = "C:\\Users\\nkv57\\OneDrive\\Desktop\\docs"

# for i in os.scandir((ways)):
#     print(i.path, i.is_dir(), i.is_file())
#  =====================================================================
# for i in os.walk(ways):
#     print(i)
#  отримуємо кортеж з шляхом і списками папок і файлів, розпаковуємо кортеж
# pathes = []
# for address, dirs, files in os.walk(ways):
#     for file in files:
#         pathes.append(os.path.join(address, file))
# print(pathes)
#  ===================================================================================
# create_time = os.path.getctime("C:\\Users\\nkv57\\OneDrive\\Desktop\\docs\\two.txt")
# print((time.time() - create_time) / 60 / 60)
# print(time.time())  #  час роботи комп. від 01.01.1970
#======================================================================================
#  пошук файлів з виключенням непотрібних папок
# path = "C:/"
# exclude_dirs = ['Windows', 'Файли програм', 'Файли програм (x86)']
# matches = []
# for address, dirs, files in os.walk(path):
#     for exclude in exclude_dirs:
#         if exclude in dirs:
#             dirs.remove(exclude)
#     for file in files:
#         if 'two.txt'in file:
#             matches.append(os.path.join(address, file))
# print(matches)
#  ==================================================================
query = input('Що шукаємо?\n>> ')
pro_time = """Введіть скільки годин назад був створений файл,
або натисніть 'enter' якщо час невідомий.
>>>
"""
time_stamp = int(input(pro_time) or 0) * 3600
time_now = time.time()
path = "C:/"
exclude_dirs = ['Windows', 'Файли програм', 'Файли програм (x86)']
matches = []
for address, dirs, files in os.walk(path):
    for exclude in exclude_dirs:
        if exclude in dirs:
            dirs.remove(exclude)
    for file in files:
        if query in file:
            full_path = (os.path.join(address, file))
            if os.path.islink(full_path):
                continue
            if time_stamp:
                if time_now - os.path.getctime(full_path) < time_stamp:
                    matches.append(full_path)
            else:
                matches.append(full_path)
if not matches:
    print('File not found.')
elif len(matches) == 1:
    print('Launch file:', matches[0])
    subprocess.run(f"start {matches[0]}", shell=True)
else:
    print('Found any files:')
    count = 0
    for i in matches:
        print(f"{count}: {i}")
        count += 1
    print('Choice file for lounch:')
    choice = int(input().strip())
    if 0 <= choice < len(matches):
        print('Launch file:', matches[choice])
        subprocess.run(f"start {matches[choice]}", shell=True)
    else:
        print('Incorrect choice.')
