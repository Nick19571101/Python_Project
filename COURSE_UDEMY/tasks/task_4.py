# задача зібрати з сайту тільки ціни товарів, програма зібрала ціни у вигляді списку з цінами як рядки. Треба перевести рядкові значення в float-type і видалити порожні значення цін

# scraped_prices = ["100,50", "5,80", "", "", "25,99", "", "17,50", "0,95", "99,00"]
# normalized_price_lst = []
# i = 0
# while i < len(scraped_prices):
#     item = scraped_prices[i]
#     if item:
#         item = float(item.replace(",", "."))
#         normalized_price_lst.append(item)

#     i += 1
# print(normalized_price_lst)
# =========ВАРІАНТ===================
scraped_prices = ["100,50", "5,80", "", "", "25,99", "", "17,50", "0,95", "99,00"]
i = 0
while i < len(scraped_prices):
    item = scraped_prices[i]
    if item:
        scraped_prices[i] = float(item.replace(",", "."))
        i += 1
    else:
        scraped_prices.pop(i)

print(scraped_prices)
result = scraped_prices
print(sum(result))
print(min(result))
print(max(result))
