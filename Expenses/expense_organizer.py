
print('Starting ...')

class Expense:
    def __init__(self, description, amount, date):
        self.description = description
        self.amount = amount
        self.date = date


def main():
    print('main() staarting ...')
    expense1 = Expense('food', 2.99, '2023-07-04')
    print('expense1: ', expense1.__dict__)

    while True:
        print('1) add expense')
        print('2) total all expenses')
        print('3) view expenses')
        selection = input('Enter selection: ')

if __name__ == "__main__":
    main()


print('Done')

