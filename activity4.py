correct_pin = 12345
balance = 2000

def cash_machine(pin_number, balance, withdrawal_amount):
    if(correct_pin == pin_number and withdrawal_amount <= balance):
        print("Take your money")
        balance -= withdrawal_amount
        print("Your updated balance is: {}".format(balance))
    elif(pin_number != correct_pin):
        print("You have entered the incorrect pin")
    elif(balance <= withdrawal_amount):
        print("You do not have enough money to withdraw")

cash_machine(12345, balance, 1000)