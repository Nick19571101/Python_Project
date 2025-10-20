#  фільтр по діапазонах
nums1 = ( 1 , 4 , 12 , 98 , 102 , - 5 , 0 , 77 , 88 )
nums2 = tuple ( range (- 10 , 25 , 3 ))

def filter_numbers(numbers, min_value=-10, max_value=100,
                   reverse=False, even_only=False):
    result = []
    for n in numbers:
        if n < min_value or n > max_value:
            continue
        if even_only and n % 2 != 0:
            continue
        result.append(n)
    result.sort()
    if reverse:
        result.reverse()
    return result
print(filter_numbers(nums1))
print (filter_numbers( nums2, even_only = True ))
print (filter_numbers( nums1 , reverse = True ))
