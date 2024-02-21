# HW1.py
# Author:

# Question 1:
# Print Hello World like we did in class
print("Hello World")
# Question 2:
# Print the following:
# Your name
print('Nanshalle Ali Smith')
# Your age
print(19)
# Your favorite color
print('blue')
# Your favorite animal
print('dogs')
# Question 3:
# Create a variable called "myName" and set it equal to your name
myName="Nanshalle"
# Create a variable called "myAge" and set it equal to your age
myAge="19"
# Create a variable called "myColor" and set it equal to your favorite color
myColor="blue"
# Create a variable called "myAnimal" and set it equal to your favorite animal
myAnimal="dogs"
# Print the following:
# Hello, my name is <myName> 
print("Hello my name is", myName)
# I am <myAge> years old
print("My age is ", myAge," years old")
# My favorite color is <myColor>
myColor= "blue"
# My favorite animal is <myAnimal>
print("my favorite animal is",myAnimal)


# Question 4:
# Calculate the following and print the result:
# 2 + 2 
print(2+2)

# 3 * 4
print(3*4)

# 5 - 6
print(5-6)

# 8 / 2
print(8/2)

# Question 5:
# Create a variable called "num1" and set it equal to 2
num1=2
# Create a variable called "num2" and set it equal to 3
num2=3
# Create a variable called "num3" and set it equal to 4
num3=4
# Create a variable called "num4" and set it equal to 5
num4=5
# Calculate the following and print the result:
# num1 + num2
(num1+num2)
# num3 * num4
(num3 * num4)
# num4 - num1
(num4 - num1)
# num2 / num1
(num2/num1)
# Question 6: Write a program that asks the user for their name and then prints the following:
user_name= input("Enter your name")
# Hello, <name>. Please enter three numbers.
print(user_name)
# The program should then ask the user for three numbers (floats) and print the following:
print("input three numbers")
flt1=float (input("number1"))
flt2=float(input("number2"))
flt3=float(input("number3"))
# 1. The sum of the three numbers is <sum>
print(flt1+flt2+flt3)
# 2. The product of the three numbers is <product>
print(flt1*flt2*flt3)
# 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3
round1=round(flt1)
round2=round(flt2)
round3=round(flt3)
print((round1+round2+round3)//3)
# 4. The average of the three numbers is <average>
print((round1+round2+round3)//3)
# Question 7: Ask the user for an input of a symbol (in the example its *) 
user=input("please input a symbol")
# Print a diamond of the symbol that looks like the following. Include the spaces and the | character.
print("        "+user+"        ",end="|\n")
print("     ",user,user,user,"    ",end="|\n")
print("   ",user,user,user,user,user,"    ",end="|\n")
print("   ",user,user,user,user,user,user,user,"  ",end="|\n")
print("   ",user,user,user,user,user,"   ",end="|\n")
print("    ",user,user,user,"     ",end="|\n")
print("    ",user,"   ",end="|\n")
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.

#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |
