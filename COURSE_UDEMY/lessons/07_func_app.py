#  =============FUNCTION - ОСНОВИ==========================
# def func():
#     x = 5
#     y = 10
#     r = x + y
#     print(r)
# # func()
# # def cube():
# #     x = 7
# #     q = x**3
# #     return q
# num = 3
# def cube(x):
#     q = x**num
#     return q
# result = cube(7)
# print(result)
#  ================================================================

# raw_url = 'example.com'

# def func(url):
#     if 'www' not in url:
#         url = 'https://www.' + url

#     elif 'https://' not in url:
#         url = 'https://' + url
#     return url
# print(func(raw_url))
#  ===============позіційні аргументи============================
# def percent(value, part):
#     if value <= 0 or part < 0:
#         print('Value can`t be 0 or less 0')
#     else:
#         percent = part / value * 100
#         print(round(percent, 2), '%')
# def percent_of(value, part, /):
#     if value <= 0 or part < 0:
#         return False
#     percent = part / value * 100
#     return str(round(percent, 2)) + ' %'
# res = percent_of(53, 142)
# print(res)
#  ====ключові, тільки ключові та позиційні аргументи===============
exchangers = (
    ["44519", 0.91],
    ["96421", 0.9],
    ["33415", 0.92],
    ["43425", 0.91],
    ["64697", 0.91],
    ["83145", 0.93],
)
exchange_rate = 0.89

def percent_of(*, value, part, numeric):
    if value <= 0 or part < 0:
        return False
    percent = round(part / value * 100, 2)
    if numeric:
        return percent
    return str(percent + " %")

percent_list = []
for exchanger in exchangers:
    percent = percent_of(exchange_rate, exchanger[1], True)
    if percent:
        percent_list.append(percent)
        exchanger.append(percent)
# print(percent_list)
# print(exchangers)

#  рефакторінг параметрів функції===================================
# def get_area_and_volume_sq(length, width, height=None):
#     area = round(length * width, 2)
#     volume = None
#     if height:
#         volume = round(area * height, 2)
#         return area, volume
# print(get_area_and_volume_sq(2, 2, height=2))
