#NAME = OYE AFOLABI OLUWAPELUMI
#matrculation =VUG/CSC/22/7824
#DEPT = COMPUTER SCIENCE

#THIS CODE WAS WRITTEN IN PYTHON TO WRITE AND READ FROA FILE AND PROPER DOCUMENTATION OF THE PROCESS

import re

# Welcome message
print("WELCOME TO PELUMI STUDENT PORTAL FOR ALL STUDENTS IN A COLLEGE")

# User details input
first_name = input("First name: ")
last_name = input("Last name: ")
surname = input("Surname: ")
age = int(input("Enter your age: "))

# Display user details
print("\nAT THIS POINT, WE WILL PRINT YOUR FIRST FEW DETAILS AND YOU WILL CARRY OUT YOUR EVALUATION")
print(f"Name: {first_name} {last_name} {surname}")
print(f"Age: {age}")

# Gmail input
try:
    for i in range(2):
        gmail = input("Enter Gmail: ")
        #password format conditions must be met
        if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', gmail):
            #FORMAT FOR GMAIL
            print("You have satisfied all conditions")
            break
        else:
            print("You have not satisfied the conditions. Please enter a valid Gmail address.")
except:
    print("Open again in 1 hour")

# Other details input
school = input("Enter school of institution: ")
dept = input("Enter your department of study: ")
course_of_study = input("Choice of study: ")

# Display user details
print(f"\nYour name is {surname} {first_name} {last_name}. You are {age} years old.")
print(f"School: {school}\nDepartment: {dept}\nCourse of Study: {course_of_study}")

# password section
try:
    for u in range(1):
        print("\nKindly fill in your required information as requested")

        # Password input function
        def password():
            print("You have only 2 trials to enter your password. If not, you will be logged out.")
            password_limit = 2
            length = 7
            password = input("Enter any password of your choice: ")
            new_password = input("Enter the same password you entered earlier: ")
            if len(password) > length:
                print("Password must be less than 7 characters.")
            else:
                print("Your password is complete.")
            for p in range(password_limit):
                if password == new_password:
                    print("You have entered the right password.")
                else:
                    print("Try again.")
except:
    print("Enter your details correctly and return to the program")

# Call the password function
password()

# GPA section
# GRADE POINT AVERAGE PART
print("\nGPA is any number from 1-5.0")
gpa = float(input("Enter your GPA result: "))
if 0 < gpa < 1.5:
    print("You are on probation. Try and improve next session.")
elif 1.5 < gpa < 2.5:
    print("You are on third class but you can still do better.")
elif 2.5 < gpa < 3.5:
    print("You are on 2nd class lower but remaining small.")
elif 3.5 < gpa < 4.5:
    print("You are on 2nd class upper.")
elif 4.5 < gpa <= 5.0:
    print("You are on first class. Congratulations!")
else:
    print("One more thing: I forgot to ask you to enter your matriculation number, so we are quickly going to generate it.")

# Writing input questions and output answers to a file
#Here you can always adjust the file path on any different laptop or personal computer , so it can save directly to the folder of your choice
file_path = r"C:\Users\Hp\Desktop\computer science document\sequential programming assignment\student_portal_output.txt"

with open(file_path, 'w') as output_file:
    output_file.write(f"Name: {surname} {first_name} {last_name}\n")
    output_file.write(f"Age: {age}\n")
    output_file.write(f"Gmail: {gmail}\n")
    output_file.write(f"School: {school}\n")
    output_file.write(f"Department: {dept}\n")
    output_file.write(f"Course of Study: {course_of_study}\n")
    output_file.write("Password set\n")
    output_file.write(f"GPA: {gpa}\n")

print(f"Output saved to {file_path}")
#here output will be saved to file path which has been set manually