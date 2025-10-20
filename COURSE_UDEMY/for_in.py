
# widgets = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "0", "#"]

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
scraped_prices = ['', '', '100,50', '5,90','', '', '25,99','', '17,55',
                  '','0,95','99,00','']
new = []
for item in scraped_prices:
    if item == '':
        continue
    if not item.replace(',', '').isdigit():
        new.clear()
        print('List is uncorrect!')
        without_price = None
        break
    item = float(item.replace(',', '.'))
    new.append(item)
else:
    without_price = len(scraped_prices) - len(new)
print(new)
print(without_price)
#  =============FOR в FOR====================
# widgets = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "0", "#"]
widgets = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"]
]
for block in widgets:
    for item in block:
        print(item.center(3), end='')
    print()
