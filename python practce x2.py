for x in range(1,7):
    y = 2*x+6;print(y)


a= 1+3
b=2-4
c= 3*4
n=5/7
o=7%5
y=4//5
z= 2**5

print(a,b,c,n,o,y)


num = []
num_3 = int(input("how many numbers do u want "))
for i in range(num_3):
    num1 = int(input("put down the num"))
    num.append(num1)
    print(num)
    a= sum(num)
    print(a)
    print(a/len(num))


b = "Hello, World!"
print(b[-5:-2])

numberss = [1,2,3,4,5,6,7,8,9,-1,-20]
numberss.sort()
print(numberss)
numberss.reverse()
print(numberss)


people:list[str] = ["mario","luigi","elon"]
people.append("trump")
print(people)

#people.clear()
#print("people")

man = [1,2,3,4,5,56]
a = []
a .append(man)
print(a)

print(man[0])
man.insert(-5,-5)
print(man)


for i in range(-2,10,2):
    print(i)

def is_palindrome(s):
    # Reverse the string
    reversed_s = s[::-1]
    # Check if the original string is equal to the reversed string
    return s == reversed_s

# Input string
input_string = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(input_string):
    print(input_string," is a palindrome.")
else:
    print(input_string,"is not a palindrome.")

is_palindrome("civic")