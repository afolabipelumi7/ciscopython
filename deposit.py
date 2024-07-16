max_lines =3

def deposit():
    while True:
        amount = input("what would you like to deposit$")
        if amount.isdigit():
            amount = int(amount)
            if amount >0:
                break
            else:
                print("amount must be graeter than 0")
        else:
            print("please enter a number")

    return amount

def get_number_of_lines():
 while True:
       lines = input("enter the numbers of lines to bet on (1- + str(max_lines +)")
  if amount.isdigit():
            amount = int(amount)
            if amount >0
                break
            else:
                print("amount must be graeter than 0")
        else:
            print("please enter a number")

    return amount






 def main():
     balance = deposit()