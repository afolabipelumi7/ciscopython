print("welcome to the pelcal,a calculator that adds ,divide, find the sqrt,and can don anything")


def add(num1,num2):
    print("you will enter 2 numbers")
    num1 = int(input("enter num 1"))
    num2 = int((input("enter num 2")))
    addition = num1 + num2
    print(addition)

add(1,2)

def sub(num1,num2):
    print("you will also enter 2 numbers subtraction")
    num1s = int(input("enter num 1"))
    num2s = int(input("enter num 2"))
    subtraction = num1s-num2s
    print(subtraction)

sub(1,2)


def mult(nunum2):
    print("you will also enter 2 numbers multiplication")
    num1ss = int(input("enter num 1"))
    num2ss = int(input("enter num 2"))
    multiplication = num1ss*num2ss
    print(multiplication)

mult(1,2)

def sqr(num1):
    print("you will enter 2 numbers sqr")
    num1sss = int(input("enter num 1"))
    sqr1 = num1sss*num1sss
    print(sqr1)

sqr(1)

def sqrt(num1):
    numt = int(input("enter value of num"))
    sqrtt = num1

def med(num1):
    print("this is for calculating median")
    num= int(input("how many numbers do you want to find the median of?"))
    for i in range(num):
     nu = float(input("enter value of num"))
     print(nu)
     print("the median of the values are",median(nu))

med(4)

