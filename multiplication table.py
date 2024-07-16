#multiplication table
print("\t\t\t\multiplication table\n")


for i in range(1,13):
    print(i,end="\t")
print()
print(".......................................................\n")

for j in range(1,13):
    for k in range(1,13):
        print(j * k , end = "\t")
    print("\n")



n = int(input("enter a number:"))
for i in range(1,21):
    print(n,"*",i,"=",n*i)