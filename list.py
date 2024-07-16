letters = ["a","b","c"]
zeros = [0] * 5
print(zeros)

combines = zeros + letters
print(combines)


#list function
numbers = list(range(20))
print(numbers)

#list are iterbale
chars = list("hello world")     #list means putting it in a [] bracket that what it means
print(chars)

#len means calculate numbers of characters
print(len(chars))

# string slicing  getting individual characters in a list
letterz = ["a","b","c","d"]
print(letterz[0])
print(letterz[0:3])
print(letters[-2])

# modifying characters in a string
letterz[0] = "A"
print(letterz)

#ind3ex to slce a string
print(letterz[ : 3])
print(letterz[: : 2])

numberz = list(range(20))
print(numbers[::2])
print(numberz[::-1])

#list unpacking
numberss = [1,2,3,4,4,4,44,4,4,]
first,second,*others = numberss
print(first)
print(others)

first = numberss[0]
second = numberss[1]
third = numberss[2]

first, *others,last = numberss
print(first,last )
print(others)


lett = ["d","e","f"]
for i in lett:
    print(i)

#enumerate lists
for u in enumerate(lett):
    print(u)

# index position but problems located in codes
item = [0,"a"]
index,letter = item
for index ,j in enumerate(lett):
    print(index,lett)


#add or removing existing itmes

ley = ["c","r","w"]
#adding
#append method = at the end of the list

ley.append("f")
print(ley)
#a letter was added at the end of the list

#add item at the specific position insert method
ley.insert(0,"-")
print(ley)
#insert method u put the index position of where you want the character of what you want to add

#removing object
# removing objects at the end of the list
# we use the pop method
ley.pop()
print(ley)

ley.pop(0)
print(ley)
#removing an object at the index position

#removing an object but you dont know its index position
#we use the remove method
ley.remove("r")
print(ley)

#del or delete method
#another way of removing an item on the list
del ley[0:3]
print(ley)

#remove all the items on the list
#clear method
ley.clear()
print(ley)


#finding index position
let = [1,2,3,3,4,5,]
print(let.index(3))
print(let.index(4))
print(let.count(3))

#count = knowing the numbers of apperances in a given lisit