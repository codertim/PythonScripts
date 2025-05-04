
import decimal
import sys


DEBUG = False
print('Starting ...')


class Expense:
    def __init__(self, description, amount, date, category=''):
        self._description = description
        self._amount = amount
        self._date = date
        self._category = category

    @property
    def description(self):
        return self._description

    @property
    def amount(self):
        return self._amount

    @property
    def date(self):
        return self._date

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @amount.deleter
    def amount(self):
        self._amount = None

    def __str__(self):
        return f'  expense amount: {self._amount}'


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add(self, expense):
        self.expenses.append(expense)


def add_expense(exp_manager):
    """ get expense details from user and add expense """
    if DEBUG == True:
        print('***** add_expense() starting ... ')
    amount = decimal.Decimal(input('  amount: '))
    desc = input('  description: ')
    date_str = input('  date: ')
    new_expense = Expense(desc, amount, date_str)
    exp_manager.add(new_expense)


def show_total_expenses(expense_manager):
    """ show total of all expenses """
    if DEBUG == True:
        print('***** show_total_expenses() starting ...')
    total = decimal.Decimal('0.00')
    for expense in expense_manager.expenses:
        total += expense.amount
    print(f'\ntotal: {total:.2f}')


def view_all_expenses(expense_manager):
    """ show all expenses """
    print("\nAll expenses ...")
    if DEBUG==True:
        print('***** view_expenses() starting ...')
    for expense in expense_manager.expenses:
        print(expense)
    if len(expense_manager.expenses) == 0:
        print('  No expenses found')


def save(expense_manager):
    """ save expenses """
    print("\nSaving ... ")
    with open('my_expenses.txt', 'w') as expenses_file:
        for expense in expense_manager.expenses:
            expenses_file.write(f'{expense.amount},')
            expenses_file.write(f'{expense.description}')
            expenses_file.write(f'{expense.date},')
            expenses_file.write('\n')
    print("\n  saving done")


def main():
    if '--debug' in sys.argv:
        DEBUG = True
    else:
        DEBUG = False

    if DEBUG == True:
        print('***** main() starting ...')
        print('  sys.argv:', sys.argv)

    expense1 = Expense('food', 2.99, '2023-07-04')
    expense_manager= ExpenseManager()


    if DEBUG == True:
        print('expense_manager __dict__: ', expense_manager.__dict__)
        print('expense test __dict__: ', expense1.__dict__)

    while True:
        print()
        print('1) add expense')
        print('2) total expenses')
        print('3) view all expenses')
        print('4) save')
        print('q) quit')

        selection = input('\nEnter selection: ')
        if selection == '1':
            add_expense(expense_manager)
        elif selection == '2':
            show_total_expenses(expense_manager)
        elif selection == '3':
            view_all_expenses(expense_manager)
        elif selection == '4':
            save(expense_manager)
        elif selection.lower() == 'q':
            print('\nDone.')
            exit()

        print('\n  item count: ', len(expense_manager.expenses))
        print()


if __name__ == "__main__":
    main()


print('Done.')

