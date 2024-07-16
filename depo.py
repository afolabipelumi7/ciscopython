#used for collecting user input gets deposit from the user
print("this program does not encourage gamblng")
print("this is for 18 years and above")


max_lines = 3
max = 100
minimum =1

def deposit():
    while True:
        amount = input("what would you like to deposit?$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("please enter a monetary value that is greater than 0")
        else:
            print(" pls enter a number")
    return amount


deposit()

def get_number_of_lines():
    while True:
        lines = input("enter number of lines you want")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= max_lines:
                break
            else:
                print("please enter a valid number of lines")
        else:
            print(" pls enter a number")
    return lines

def get_bet():
    while True:
        amount = input("what would you like to bet on each line ?$")
        if amount.isdigit():
            amount = int(amount)
            if minimum <= amount <= max:
                break
            else:
                print(f"amount  must be between {minimum} and {max}")
        else:
            print(" pls enter a number")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

    if total_bet > balance:
        print(f"unfortunately you do not have enough in your balance, your current balance is:",{balance})
    else:
        print("you are fine")
    
    print(f"you are betting ${bet} on {lines} lines.total bet is equal to: {total_bet} ")
    print("my balance is ",balance,"the lines you picked is",lines)

main()

