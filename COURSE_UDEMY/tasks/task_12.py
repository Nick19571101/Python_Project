#  релізувати універсальну функцію, яка обчислюєсередньоарифметичне значення всіх переданих аргументів

temps_celsius = [-1.5, 0.2, 2.8, 5.6, 8.4, 11.2, 14.7, 17.0, 18.3, 19.1, 19.4, 18.8, 17.0, 14.5, 11.2, 7.8, 4.0]

def average_value(*args, rounding=2):
    if not args:
        raise ValueError('args can not be empty')
    return round(sum(args) / len(args), rounding)


# print(average_value(*temps_celsius))
#  складніше обчислення ==========================================================

temps_groups = [
    [12.4, 13.6, 15.1],
    [8.3, 9.1],
    [20.0],
    [],
    [0, -2, 1, 5]
]
def average_value(*args, rounding=2):
    if not args:
        return None
    return round(sum(args) / len(args), rounding)
temporary_list = []
for group in temps_groups:
    temporary_list.extend(group)

print(average_value(*temporary_list))
