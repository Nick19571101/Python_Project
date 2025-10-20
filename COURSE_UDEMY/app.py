# cash = 287  #  100, 50, 20, 5, 1
# hundreds = cash // 100  #  2
# rest_off = cash % 100  # 87
# fifties = rest_off // 50  # 1
# rest_off = rest_off % 50  #  37
# twenties = rest_off // 20  #  1
# rest_off = rest_off % 20  # 17
# fives = rest_off // 5  #  3
# rest_off = rest_off % 5  #  2
# ones = rest_off
# print(hundreds, fifties, twenties, fives, ones)
# res = round(237 / 48, 2)
# print(res)
# import math
# x = 3.456
# res_2 = math.ceil(x)  #  округлення в більшу сторону
# print(res_2)
# res_3 = math.floor(x)  #  округлення в меншу сторону
# print(res_3)
#  ============превірка приналежності  і ідентичності, порівняння==============
# 5 == 5  #  True
# 5 < 7  #  True
# 5 != 5  # False
# num = 2 + 2 > 5  #  False
# url = "www.google.com"
# print("www" in url)  #  True
#  not x == x   логічне нє
#  'www.' not in 'google.com'c
#  if - elif - else - statement - інструкція, оператор
# x = 7
# if x == 0:
#     print("You can't divide by zero")
# else:
#     print(100/x)
#  вирахування процентів
# value = float(input('Value: '))
# part = float(input('How many?: '))
# if value <= 0:
#     print('Value cant be zero or less zero')
# elif part < 0:
#     print('Part cant be less zero')
# else:
#     percent= part / value * 100
# print(round(percent, 2), '%')

# x = 5
# y = 7
# if x >= 0 and y >= 0:
#     print(x*y)

# user_input = 'Hello'
# word = 'hello'
# if word in user_input.lower():
#     print('Hello')

# url ='http://google.com'
# url = url.replace('http:', 'https:')
# print(url)

#  ===============ФОРМАТУВАННЯ РЯДКІВ=========================
# name = 'Alex'
# id = 1234567
# message = f"Hello {name}, your id is: {id}"
# print(message)
# #  ================PALINDROME===================
# word = 'level'
# # is_palindrome = word == word[::-1]
# # print(is_palindrome)
# i = 0
# j = len(word) - 1
# is_palindrome = True
# while i < j:
#     if word[i] != word[j]:
#         is_palindrome = False
#         break
#     i += 1
#     j -= 1
# print(is_palindrome)
# ==================ЦИКЛИ-WHILE==================================
# count = 0
# while count <= 7:
#     print(count)
#     count +=1

# password = input('Create your password:\n')

# while True:
#     if len(password) <= 8:
#         print('Password must be at least 8 characters long')
#         password = input('Enter your password again:\n')
#     else:
#         break
# print(password)
#  ====================КОРТЕЖ(tuple)=====================
# data = ('Home', 'Catalog', 'Payment', 'About')

# print(data)
# print(data[3])
# data = data + ('abc', 'nmh')
# print(data)
# date = ('15', 'August', '2025')
# day, month, year = (15, 'August', 2025)  #  розпаковка кортежу
# day, *other = (15, 'August', 2025)  #  розпаковка кортежу
# print(f'It is {day} {month} {year}')
# print(other)
# T ='-=-'.join(date)  #  15-=-August-=-2025
# print(T)
#  ===========ЗМІНЮВАНИЙ ТИП ДАНИХ(СПИСОК - list)================
# numbers = list()
# numbers = []
# data_list = [2, 4, 6, 8, 10]
# print(len(data_list), type(data_list))
# prices = [5.25, 15.99, 100.25, 1.55, 17.15]
#  створити новий список із скидками,використаєм while
# discount_prices = []
# discount = 0.9

# i = 0
# while i < len(prices):
#     discount_prices += [round(prices[i] * discount, 2)]
#     i += 1
# print(discount_prices)
# add_prices = [7.99, 8.89]
# prices.extend(add_prices)
# prices.append(160)
# # prices.remove(15.99)
# # x = prices.pop(1)
# new = prices.copy()
# prices[0] = 0
# print(prices)
# print(new)
# # print(x)
#  =====================ЦИКЛИ-FOR_IN=======================
# ----------------порівняння while vs for------------------


# widgets = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "0", "#"]
# index = 0
# n = len(widgets)
# while index < n:
#     widget = widgets[index]
#     if index % 3 == 0 and index != 0:
#         print()
#     print(widget.center(3), end="")
#     index += 1

# else:
#     print()
# x = widgets.__iter__()
# centered_widgets = []
# for item in widgets:
#     new = item.center(3)
#     centered_widgets.append(new)

# print(centered_widgets)  # [' 1 ', ' 2 ', ' 3 ', ...]
# =========робимо сітку============

# for item in widgets:
#     #  i = widgets.index(item)
#     if widgets.index(item) % 3 == 0 and widgets.index(item) != 0:
#         print()
#     print(item.center(3), end='')

# else:
#     print()
#  ============ПОВНА ФОРМА ЦИКЛУ З CONTINUE, BREAK================
# scraped_prices = ['', '', '100,50', '5,90','', '', '25,99','', '17,55',
#                   '','0,95','99,00','']
# new = []
# for item in scraped_prices:
#     if item == '':
#         continue
#     if not item.replace(',', '').isdigit():
#         new.clear()
#         print('List is uncorrect!')
#         without_price = None
#         break
#     item = float(item.replace(',', '.'))
#     new.append(item)
# else:
#     without_price = len(scraped_prices) - len(new)
# print(new)
# print(without_price)

#  =============FOR в FOR====================
# widgets = [
#     ["1", "2", "3"],
#     ["4", "5", "6"],
#     ["7", "8", "9"],
#     ["*", "0", "#"]
# ]
# x = widgets[0][1]
# print(x)
# for block in widgets:
#     for item in block:
#         print(item.center(3), end='')
#     print()
#  ================RANGE()=======================
# x = list(range(51, -2, -2))
# print(x)
# #  [51, 49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, -1]
#  ============practice range and for=====================
# import currencies as cur

# for i in range(0, len(cur.currencies) -1, 1):
#     # value = cur.currencies[i]
#     # print(value) #  видалення елементу по його індексу
#     if cur.currencies[i][0] == 'PHP':
#         el = cur.currencies.pop(i)
# print(el)
# #  len(cur.currencies) -1, -1, -1
#  ===========ПОРІВНЯННЯ КОРТЕЖІВ І СПИСКІВ=====================
# x = (1, 2, 5, 10, -50, -50, 151)
# y = list(x)
#  y = [1, 2, 5, 10, -50, -50, 151]
#  це є несумісні послідовності
# import copy
# x = [[1, 2], 5, 10, -50, -50, 151]
# y = copy.deepcopy(x)
# x[0].clear()
# print(y)
# print(x)
#  ========використання функції os.system python====================
# import os
# x = os.system('ping localhost')
# print(x)
# print('Next code!')
#  =================SUBPROCESS PYTHON===============================
# import os
# import subprocess
# from sys import stderr, stdout

# x = os.system('python myapp.py')
# x = subprocess.run('python myapp.py', shell=True)
# command = ["python", "myapp.py"]
# x = subprocess.run(command)
# x = subprocess.Popen(command)
# x = subprocess.run(command, stdout=subprocess.PIPE, text=True, encoding='utf-8')
#  ===========для однократних процесів=============================================
# x = subprocess.Popen(command, stdout=subprocess.PIPE, text=True, encoding='utf-8')
# stdout, stderr = x.communicate()
# print(stdout.strip() , 'Whoa!')
# ============для багаторазових процесів(безкінечних)
# x = subprocess.Popen(command, stdout=subprocess.PIPE, text=True, encoding="utf-8")
# for item in x.stdout:
#     print(item.strip() + " Whoa!")
# print("Code done!")
# x = os.popen('ping localhost')
# print(x.read().encode('cp1251').decode('cp866'))
#  =====================shell ін'єкція===========================================
# user_input = input('Enter host: ')

# # os.system(f"ping -c 1 {user_input}")
# subprocess.run((['ping', '-c', '1', user_input]))
#  ===============module shutil===================================================
# import shutil


# shutil.copy2("C:\\Users\\nkv57\\Desktop\\password.txt", "C:\\Users\\nkv57\\Desktop\\docs\\passwords\\" )
# shutil.make_archive("C:\\Users\\nkv57\\Desktop\\dst_backup","zip",
#                     "C:\\Users\\nkv57\\Desktop\\docs")
#  ==========структура коду(практика)=============================================
def get_data():
    return (
        ["44519", 0.91],
        ["96421", 0.9],
        ["33415", 0.92],
        ["43425", 0.91],
        ["64697", 0.91],
        ["83145", 0.93],
    )


def get_exchange_rate():
    return 0.89


def get_percent_of(value, part):
    if value <= 0 or part < 0:
        return False
    return round(part / value * 100, 2)


def get_processed_data():
    percent_list = []
    exchangers = get_data()
    exchange_rate = get_exchange_rate()
    for exchanger in exchangers:
        percent = get_percent_of(exchange_rate, exchanger[1])
        if percent:
            percent_list.append(percent)
            exchanger.append(percent)
    return percent_list, exchangers


# x, y = get_processed_data()
# print(x)
# print(y)
#  ======== * як аргумент ==============================================
def multiply(*values):
    res = 1
    for i in values:
        res *= i
    return res


x = multiply(1, 2, 3, 4)
# print(x)
#  ==========import, import from - простір імен===========================
# import sys
# print(sys.path)
# import random
#  ======практика з імпорту і структури коду==============================
# from communicate import get_username, get_password
# data_base = []
# def delete_user():
#     pass
# def login():
#     pass
# def logout():
#     pass
# def create_user():
#     username = get_username()
#     password = get_password()
#     user = username, password
#     data_base.append(user)

# create_user()
# print(data_base)
#  =====аргументи як ситуативні вирази======================================
from time import strftime

locale = "en_US"


# print(strftime("%H:%M>%S %Y"))
def pretty_time(
    *, date_delimeter=".", time_delimeter=":", time_first=False, us_format=False
):
    if us_format:
        date_format = f"%m{date_delimeter}%d{date_delimeter}%Y"
        time_format = f"%I{time_delimeter}%M{time_delimeter}%S %p"
    else:
        date_format = f"%d{date_delimeter}%m{date_delimeter}%Y"
        time_format = f"%H{time_delimeter}%M{time_delimeter}%S"
    # if time_first:
    #     pattern = f"{time_format} {date_format}"
    # else:
    #     pattern = f"{date_format} {time_format}"
    pattern = (
        f"{time_format} {date_format}" if time_first else f"{date_format} {time_format}"
    )
    return strftime(pattern)


time_now = pretty_time(us_format=True)
print(time_now)

