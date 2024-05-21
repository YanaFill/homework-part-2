import time
from threading import Lock, Thread
import threading, random
from time import perf_counter


class BankAccount:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} поповнив рахунок на {amount} грн. Новий баланс: {self.balance} грн.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} зняв {amount} грн. Новий баланс: {self.balance} грн.")
            return True
        else:
            print(f"{self.name} не може зняти {amount} грн. Недостатньо коштів на рахунку.")
            return False

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} поповнив рахунок на {amount} грн. Новий баланс: {self.balance} грн.")

    def get_balance(self):
        return self.balance

class ATM:
    def __init__(self, money):
        self.money = money
        self.lock = threading.Lock()

    def replenish(self, amount):
        self.lock.acquire()
        self.money += amount
        print(f"Банкомат поповнений на {amount} грн. Новий баланс: {self.money} грн.")
        self.lock.release()

    def withdraw(self, account, amount):
        self.lock.acquire()
        if account.withdraw(amount) and self.money >= amount:
            self.money -= amount
            print(f"З банкомату знято {amount} грн.")
            self.lock.release()
            return True
        else:
            self.lock.release()
            return False

    def deposit(self, account, amount):
        self.lock.acquire()
        account.deposit(amount)
        self.money += amount
        print(f"На рахунок {account.name} внесено {amount} грн.")
        self.lock.release()


def user_operation(atm, account, operation, amount):
    if operation == "withdraw":
        atm.withdraw(account, amount)
    elif operation == "deposit":
        atm.deposit(account, amount)

accounts = [
    BankAccount(1, "Іван", 1000),
    BankAccount(2, "Петро", 500),
    BankAccount(3, "Олена", 2000),
]

atm = ATM(5000)
start_time = perf_counter()
threads = []
for account in accounts:
    operation = random.choice(["withdraw", "deposit"])
    amount = random.randint(100, 500)
    thread = threading.Thread(target=user_operation, args=(atm, account, operation, amount))
    threads.append(thread)
    thread.start()

time.sleep(4)
atm.replenish(1000)

for thread in threads:
    thread.join()

total_balance = 0
for account in accounts:
    total_balance += account.get_balance()
end_time = perf_counter()
print(f"Загальний залишок на рахунках: {total_balance} грн.")
print(f"Загальний залишок у банкоматі: {atm.money} грн.")
print(f"Час виконання програми: {end_time - start_time}")
