
print('Starting ...')

class Expense:
    def __init__(self, description, amount, date):
        self.description = description
        self.amount = amount
        self.date = date

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


def show_total_expenses():
    print('***** show_total_expenses() starting ...')


def view_expenses():
    print('***** view_expenses() starting ...')



def main():
    print('***** main() staarting ...')
    expense1 = Expense('food', 2.99, '2023-07-04')
    expense_manager= ExpenseManager()

    print('expense_manager: ', expense_manager.__dict__)
    print('expense1: ', expense1.__dict__)

    while True:
        print('1) add expense')
        print('2) total all expenses')
        print('3) view expenses')
        selection = input('Enter selection: ')
        if selection == '1':
            add_expense(expense_manager)
        elif selection == '2':
            show_total_expenses()
        elif selection == '3':
            view_expenses()
        print('expenses now size: ', len(expense_manager.expenses))


if __name__ == "__main__":
    main()


print('Done')
