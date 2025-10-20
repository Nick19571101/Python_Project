cash = 777
banknotes_in_atm = [100, 50, 20, 5, 1]
def get_banknote_counts(cash, banknotes_list):
    banknotes_counts = []
    for banknote in banknotes_list:
        quantity = cash // banknote
        cash = cash % banknote
        banknotes_counts.append(quantity)
    return banknotes_counts
print(get_banknote_counts(cash, banknotes_in_atm ))
