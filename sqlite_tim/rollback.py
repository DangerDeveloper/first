class Accounts(object):

    def __init__(self, name: str, opening_balance: float = 0.0):
        self.name = name
        self._balance = opening_balance
        print(f'Account created for {self.name}', end='')
        self.show_balance()

    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            self._balance += amount
            print(f'{amount} Deposited')
            return self._balance

    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f'{amount} Withdraw')
            return amount  # It may be self._balance
        else:
            print('The amount must be greater than zero and no more than your account balance.')
            return 0.0

    def show_balance(self):
        print(f'Balance on account {self.name} is {self._balance}')
        # print(f'Balance on account {self.name} is {(self._balance / 100):.2f}')  # 0.00
        # print(f'Balance on account {self.name} is {round((self._balance / 100), 2)}')  # 0.0
        # print(f"Balance on account {self.name} is {format((self._balance / 100), '.2f')}")  # 0.00


# print(format((100/44), '.2f'))
# print(round((100/44), 2))
# print(f'{(100 / 44):.2f}')
# print(f'{round((100/44), 2)}')

if __name__ == '__main__':
    ajay = Accounts('Ajay')
    ajay.deposit(10.10)
    ajay.deposit(0.10)
    ajay.deposit(0.10)
    ajay.withdraw(0.30)
    ajay.withdraw(0)
    ajay.show_balance()
