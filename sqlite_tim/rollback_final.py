import sqlite3
import datetime
import pytz

db = sqlite3.connect('accounts.sqlite')
db.execute("CREATE TABLE IF NOT EXISTS accounts"
           " (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history"
           " (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, time TIMESTAMP NOT NULL,"
           " account TEXT NOT NULL, amount INTEGER NOT NULL, UNIQUE (time, account, id))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS "
           " SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
           " history.account, history.amount FROM history ORDER BY history.time")


class Accounts(object):

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())
        # local_time = pytz.utc.localize(datetime.datetime.utcnow())
        # return local_time.astimezone()

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute('SELECT name, balance FROM accounts WHERE (name = ?)', (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print(f'Retrieved record for {self.name} ', end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute('INSERT INTO accounts VALUES(?, ?)', (name, opening_balance))
            cursor.connection.commit()
            print(f'Account created for {self.name} ', end='')
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Accounts._current_time()
        try:
            db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            db.execute("INSERT INTO history (time, account, amount) VALUES(?, ?, ?)",
                       (deposit_time, self.name, amount))
        except sqlite3.Error:
            db.rollback()
        else:
            db.commit()
            self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            # new_balance = self._balance + amount
            # deposit_time = Accounts._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(amount)
            print(f'{(amount / 100):.2f} Deposited')
            return self._balance

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            # new_balance = self._balance - amount
            # withdrawal_time = Accounts._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (withdrawal_time, self.name, -amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(-amount)
            print(f"{format((amount / 100), '.2f')} Withdraw")
            return amount / 100  # It may be self._balance
        else:
            print('The amount must be greater than zero and no more than your account balance.')
            return 0.0

    def show_balance(self):
        print(f'Balance on account {self.name} is {(self._balance / 100):.2f}')  # 0.00


if __name__ == '__main__':
    ajay = Accounts('Ajay')
    ajay.deposit(1010)
    ajay.deposit(10)
    ajay.deposit(10)
    ajay.withdraw(30)
    ajay.withdraw(0)
    ajay.show_balance()

    ankur = Accounts('Ankur', 5666)
    vikrant = Accounts('Vikrant', 3456)
    rahul = Accounts('Rahul', 2222)
    vik = Accounts('Vik')
    imran = Accounts('Imran')
    bharat = Accounts('Bharat')

    db.close()
