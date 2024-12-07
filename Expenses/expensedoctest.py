


class Expense:
    def __init__(self, description, amount, date):
        """
        >>> expense1 = Expense('desc1', '9.97', '2020-01-02')
        >>> expense1._description
        'desc1'
        """
        self._description = description
        self._amount = amount
        self._date = date

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    def __str__(self):
        return f'amount: {self._amount}'


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add(self, expense):
        self.expenses.append(expense)




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
