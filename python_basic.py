
# Printing a name
print("Chaitanya")


# Taking user input for name
name = input("enter your name: ")

# Displaying the entered name
print("name:" + name)


# Declaring two numbers
a = 10
b = 5

# Arithmetic operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


# Taking marks input from user
marks = int(input("Enter marks: "))

# Checking grade using if-else
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# For loop from 1 to 5
for i in range(1, 6):
    print(i)


# While loop from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1


# List example
students = ["Chaitanya", "ketan", "Shub"]

# Printing list
print(students)

# Printing second element from list
print(students[1])


# Tuple example
fruits = ("mango", "apple", "pineapple")

# Printing tuple
print(fruits)


# Set example
myset = {1, 2, 3}

# Printing type of set
print(type(myset))


# Dictionary example
student = {
    "name": "Chaitanya",
    "age": 19
}

# Printing dictionary
print(student)


# Function for division
def division(x, y):
    return x / y

# Calling function
result = division(10, 5)

# Printing result
print("the division of two number is", result)