
print('Starting ...')

class Expense:
    def __init__(self, description, amount, date):
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


def add_expense(exp_manager):
    print('***** add_expense() starting ... ')
    amount = float(input('  amount: '))
    desc = input('description: ')
    date_str = input('date: ')
    new_expense = Expense(desc, amount, date_str)
    exp_manager.add(new_expense)


def show_total_expenses(expense_manager):
    """ show total of all expenses """
    print('***** show_total_expenses() starting ...')
    total = 0.0
    for expense in expense_manager.expenses:
        total += expense.amount
    print(f'total: {total:.2f}')

def view_expenses(expense_manager):
    print('***** view_expenses() starting ...')
    for expense in expense_manager.expenses:
        print(expense)



def main():
    print('***** main() staarting ...')
    expense1 = Expense('food', 2.99, '2023-07-04')
    expense_manager= ExpenseManager()

    print('expense_manager: ', expense_manager.__dict__)
    print('expense1: ', expense1.__dict__)

    while True:
        print()
        print('1) add expense')
        print('2) total all expenses')
        print('3) view expenses')
        print('q) quit')

        selection = input('Enter selection: ')
        if selection == '1':
            add_expense(expense_manager)
        elif selection == '2':
            show_total_expenses(expense_manager)
        elif selection == '3':
            view_expenses(expense_manager)
        elif selection.lower() == 'q':
            print('\nDone.')
            exit()

        print('expenses count: ', len(expense_manager.expenses))
        print()


if __name__ == "__main__":
    main()


print('Done')

