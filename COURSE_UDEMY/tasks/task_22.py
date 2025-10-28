"""Створити клас що описує гаманець цифрових грошей користувача
Атрибути:
        owner (str): ім'я власника
        wallet_id (str): унікальний ідентифікатор гаманця
        currency (str): валюта гаманця
        balance (float): поточний баланс
"""

import random
import string


class Wallet:
    def __init__(self, owner: str, currency: str = "USD"):
        self.owner = owner
        self.currency = currency
        self.wallet_id = self.create_id()
        self.balance = 0.0

    def create_id(self):
        """Створює унікальний ID довжиною 8 символів, що складається з цифр і літер."""
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def replenish_depo(self, amount: float | int):
        """Поповнює рахунок на задану суму
        Args: amount (float): сума поповнення
        """
        if amount <= 0:
            print("Сума поповнення має бути!!!")
            return False
        self.balance += amount
        return self

    def withdrow(self, amount: float | int):
        """списує кошти з рахунку
        Args:amount (float): сума списання
        """
        if amount <= 0:
            print("Сума списання має бути!")
            return False
        if amount > self.balance:
            print(f"Недостатньо коштів. Баланс: {self.balance}")
            return False
        self.balance -= amount
        return self

    def transfer_target(self, target_wallet: "Wallet", amount: float | int):
        """Переказує кошти на інший гаманець.
        Args:
            target_wallet (Wallet): екземпляр іншого гаманця
            amount (float): сума переказу
        """
        if self.currency != target_wallet.currency:
            print("Переказ неможливий між гаманцями з різною валютою")
            return False
        self.withdrow(amount)
        target_wallet.replenish_depo(amount)
        return self

    def __add__(self, amount: float | int):
        """Дозволяє поповнити гаманець через оператор +"""
        self.replenish_depo(amount)

    def __sub__(self, amount: float | int):
        """Дозволяє зняти кошти з гаманця через оператор -"""
        self.withdrow(amount)

    def __str__(self):
        # return str(self.balance)
        return f"{self.owner}'s Wallet | ID: {self.wallet_id} | {self.balance:.2f} {self.currency}"


x = Wallet("ABC").replenish_depo(100)
print(x.balance)
