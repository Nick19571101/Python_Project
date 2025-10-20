import os
path = "C:\\Users\\nkv57\\OneDrive\\Desktop\\docs"

# x = os.scandir(path)
# print(x)
# for i in os.scandir(path):
    # print(i.path, i.is_dir(), i.is_file())
# C:\Users\nkv57\OneDrive\Desktop\docs\keys True False
# C:\Users\nkv57\OneDrive\Desktop\docs\one.txt False True
# C:\Users\nkv57\OneDrive\Desktop\docs\passwords True False
# C:\Users\nkv57\OneDrive\Desktop\docs\two.txt False True
# for i in os.walk(path):
#     print(i)
# ('C:\\Users\\nkv57\\OneDrive\\Desktop\\docs', ['keys', 'passwords'], ['one.txt', 'two.txt'])
# ('C:\\Users\\nkv57\\OneDrive\\Desktop\\docs\\keys', ['secret_key'], [])
# ('C:\\Users\\nkv57\\OneDrive\\Desktop\\docs\\keys\\secret_key', [], ['key.txt'])
# ('C:\\Users\\nkv57\\OneDrive\\Desktop\\docs\\passwords', [], ['password.txt'])
paths = []
for address, dirs, files in os.walk(path):
    for file in files:
        if '.txt' in file:  #  тільки для файлів .txt
            paths.append(os.path.join(address, file))
print(paths)
# C:\Users\nkv57\OneDrive\Desktop\docs\one.txt
# C:\Users\nkv57\OneDrive\Desktop\docs\two.txt
# C:\Users\nkv57\OneDrive\Desktop\docs\keys\secret_key\key.txt
# C:\Users\nkv57\OneDrive\Desktop\docs\passwords\password.txt

# ['C:\\Users\\nkv57\\OneDrive\\Desktop\\docs\\one.txt', 'C:\\Users\\nkv57\\OneDrive\\Desktop\\docs\\two.txt', 'C:\\Users\\nkv57\\OneDrive\\Desktop\\docs\\keys\\secret_key\\key.txt', 'C:\\Users\\nkv57\\OneDrive\\Desktop\\docs\\passwords\\password.txt']
