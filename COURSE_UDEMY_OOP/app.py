# arr =tuple([2, 3])
# def add_first(x):
#     if type(x) == tuple:
#         x = list(x)
#     x.insert(0, 1)
#     return x
# y = add_first(arr)
# print(arr)
# print(y)
#  функція isinstance - переввірка на тип====================================
# def multiply(*args: int | float | list | tuple):
#     result = 1
#     for item in args:
#         if isinstance(item, list):
#             for i in item:
#                 result *= i
#         else:
#             result *= item
#     return result


# x = [6, 7, 8, 9, 10]
# print(multiply(1, 2, 3, 4, 5))
# print(multiply(x))
# # зберігання атрибутів об'єкту. Словник (dict)
# data = {'name': 'Bob', 'age': 25}
# data['age'] = 33
# data['salary'] = 10000
# # del data['salary']
# for key in data:
#     print(key)
# #     print(data[key])
#  ================концепція ООП==================================
# class MyClass(object):
#     w = 7
# x = MyClass()
# print(x)
# class Counter:
#     def set(self, value):
#         # print('abracadabra')
#         self.count = value
#     def get(self):
#         return self.count
#     def __str__(self):
#         return str(self.count)
# x = Counter()
# y = Counter()
# x.set(169)
# # print(x.__dict__)
# # print(y.__dict__)
# # print(x.count)
# # print(x.get())
# print(x)
#  -------------------- __init__() -------------------------------
# class Counter:
#     def __init__(self, value):
#         self.count = value
#     def __str__(self):
#         return str(self.count)
# x = Counter(160)
# print(x)
# ===========практика, створення класу =============================
import os
from pathlib import Path
# from pathlib import Path
# x = Path(__file__)  ##  маємо поточний файл
# print(x)

# class Path:
#     def __init__(self):
#         self.CWD = os.getcwd()
#         self.current = os.path.dirname(__file__)
#     def parent(self):
#         self.current = os.path.dirname(self.current)
#         return self
#     def get_parent(self):
#         return os.path.dirname(self.current)
#     def add_dir(self, dirname):
#         self.current =os.path.join(self.current, *dirname)
#         return self
# path = Path().parent().add_dir(('test', 'test2'))
# # print(path.CWD)
# print(path.current)
# =============методи операторів, перегрузкеа операторів================
class Path:
    def __init__(self, path):
        self.current = path or os.path.dirname(__file__)
    def parent(self):
        self.current = os.path.dirname(self.current)
        return self
    def get_path(self):
        return self.current
    # def __add__(self, obj):
    #     self.current = os.path.join(self.current, obj)
    #     return self
    # def __add__(self, obj):
    #     return Path(os.path.join(self.current, obj))
    def __add__(self, obj):
        if isinstance(obj, str):
            return Path(os.path.join(self.current, obj))
        elif isinstance(obj, Path):
            return Path(os.path.join(self.current, obj.current))
    def __str__(self):
        return self.current
path = Path("C:\\Users\\nkv57\\Desktop\\COURSE_UDEMY_OOP")
# path2 = path + 'test'
path2 = path + Path('user')
# print(path + 'test')
print(path)
print(path2)
