def greet():
    print("Hello,welcome to internship")

greet()


#arguments and Return values

def add_num(a,b):
    return a+b
result=add_num(4,5)
print(result)


#local and global 


x=10
def fun():
    print(x)

fun()
print(x)

#example
veg="panner"
fruit="mango"
def display():
    mix="salad"
    print(mix)
display()
print(veg)
print(fruit)


#importing standard modules

import math
import random

print(math.sqrt(16))
print(random.randint(1,10))

#creating and importing custome modules


#task1

def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))  

area, perimeter = calc_rectangle(length, width)
print("The area of the rectangle is: ", area)
print("The perimeter of the rectangle is: ", perimeter)


