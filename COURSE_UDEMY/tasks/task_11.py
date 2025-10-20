#  перетворення списку з чисел в список з рядків============================
# data_int = [1, 2, 5, 10, 20, 100]
# def convert_list_values(arr):
#     arr = arr.copy()
#     new_arr = []
#     for item in arr:
#         new_arr.append(str(item))
#     return new_arr
# data_str = convert_list_values(data_int)
# print(data_str)
#  складне перетворення списку==============================================
data = [32,34,33,24,22,25,26,26,27,52,53,25]
def to_matrix(arr, columns=3):
    if not len(arr):
        return False
    temp_data = []
    start = 0
    stop = columns
    while True:
        part = arr[start:stop]
        if part:
            temp_data.append(part)
        if len(part) < columns:
            break
        start = stop
        stop += columns
    arr.clear()
    arr.extend(temp_data) 
    return True
to_matrix(data)
print(data)
