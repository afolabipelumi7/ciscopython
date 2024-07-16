#even numbers
count = 0
for i in range(10):
    if i % 2 ==0:
        count += 1
        print(i)
print(f"we have {count} even numbers")

# odd
county = 0
for ii in range (50):
    if ii % 3==0:
        county += 1
        print(ii)
        
print(f"we have{county} odd numbers ")

# determination of even and odd numbers



try:
    for i in range(20):
        number = int(input("enter any number?"))
        if number % 2 == 0:
            print("its an even number")
        else:
            print("number is an odd number")
except:
    print("enter an integer value")


a,b,c = 1,2,3
if a>b:
    print("a is greater than b")
else:
    print("a is not greater than b ")



