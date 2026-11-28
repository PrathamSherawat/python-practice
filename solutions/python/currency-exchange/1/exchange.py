def exchange_money(budget, exchange_rate):
    return budget/exchange_rate
    # pass

def get_change(budget, exchanging_value):
    return budget - exchanging_value
    # pass

def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills
    # pass


def get_number_of_bills(amount, denomination):
    return amount// denomination
    # pass


def get_leftover_of_bills(amount, denomination):
    return amount % denomination
    # pass


def exchangeable_value(budget, exchange_rate, spread, denomination):
    a = exchange_rate * (1 + spread / 100)
    b = budget/a
    return int((b // denomination) * denomination)

