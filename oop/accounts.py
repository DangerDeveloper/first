import datetime
import pytz


class Accounts:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Accounts._current_time(), balance)]
        print('Account Created for ' + self._name)

    def deposit(self, balance):
        if balance > 0:
            self.__balance += balance
            self.show_balance()
            self._transaction_list.append((Accounts._current_time(), balance))

    def withdraw(self, balance):
        if 0 < balance <= self.__balance:
            self.__balance -= balance
            self._transaction_list.append((Accounts._current_time(), -balance))
        else:
            print('The amount must be greater than zero and no more than your account balance')
        self.show_balance()

    def show_balance(self):
        print('Balance is {}'.format(self.__balance))

    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print('{:6} {} on {} (local time was {})'.format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    ajay = Accounts('Ajay', 0)
    ajay.show_balance()

    ajay.deposit(1000)
    ajay.deposit(100)
    ajay.withdraw(40)
    ajay.show_transaction()

    rahul = Accounts('Rahul', 500)
    rahul.deposit(200)

    # we can override a balance instance so we use _balance for show it is use
    # only inside the class
    # rahul.balance = 100

    # _balance only to show that it is only for use inside the class
    # but we can access it any way
    # rahul._balance = 100

    # __balance create a new instance in the class do not modify the class
    # __balance because inside the class the use of __balance converted
    # into _Accounts__balance if we want to modify the __balance instance
    # outside the class we use _Accounts__balance instance which is converted by python
    # inside the class we use __balance. At the end we can change the value there is no such
    # thing as private in python
    # we can also change private value in java but it is hard
    rahul.__balance = 100

    rahul.deposit(300)
    rahul.withdraw(700)
    rahul.show_transaction()
    rahul.show_balance()
    print(rahul.__dict__)
