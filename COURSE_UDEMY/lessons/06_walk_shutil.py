import shutil
import subprocess
import time
import os

query = input("Що шукаємо?\n>> ")
pro_time = """Введіть скільки годин назад був створений файл,
або натисніть 'enter' якщо час невідомий.
>>>
"""
time_stamp = int(input(pro_time) or 0) * 3600
time_now = time.time()
path = "/"
exclude_dirs = ["Windows", "Файли програм", "Файли програм (x86)"]
matches = []
for address, dirs, files in os.walk(path):
    for exclude in exclude_dirs:
        if exclude in dirs:
            dirs.remove(exclude)
    for file in files:
        if query in file:
            full_path = os.path.join(address, file)
            if os.path.islink(full_path):
                continue
            if time_stamp:
                if time_now - os.path.getctime(full_path) < time_stamp:
                    matches.append(full_path)
            else:
                matches.append(full_path)
if not matches:
    print("File not found.")
else:
    destination = input("Куди копіювати:\n>>> ")
    print(f"Копіюю файли в {destination}")

    for file in matches:
        file_name = file.split(os.path.sep)[-1]
        dst_file_name = os.path.join(destination, file_name)
        count = 2

        while os.path.exists((dst_file_name)):
            dst_file_name = os.path.join(
                destination, file_name.replace(".", f"({count}).", count=1)
            )
            count += 1
        shutil.copy2(file, dst_file_name)

shutil.make_archive("C:\\Users\\nkv57\\Desktop\\dst_backup", "zip", destination)
