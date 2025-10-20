from copy import deepcopy

x =list(range(10))

def func(arr):
    new_arr = deepcopy(arr)
    new_arr.append(555)
    return new_arr
print(func(x))
print(x)
