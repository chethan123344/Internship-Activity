
#variables
age=21;
print(age);
height=5.8;
print(height);
name="chethan";
print(name);
is_student="true";
print(is_student)


#operators
a=int(input("Enter the first number:"));
b=int(input("Enter the second number:"));
op = input("Enter operator (+, -, *, /): ");

if op == "+":
    print("Result:", a + b);

elif op == "-":
    print("Result:", a - b);

elif op == "*":
    print("Result:", a * b);

elif op == "/":
    print("Result:", a / b);

else:
    print("Invalid operator");


#String & Type Casting
name=input("Enter your name :")
age =input("Enter your age:")
age=int(age)
age_in_2030=age+4;

print(f"Hello, My name is {name} and I'm {age} years old.")
print(f"Hey {name}, you will be{age_in_2030} years old in 2030.")


#Task 2
a=float(input("Enter the Amount:"));
b=int(input("Enter the number of people:"))
share=a/b;
print(f"Total bill {a}. Each person pays: {share}");

print(float(a))
print(int(b))
print(share)


#Task 3
item_name="Laptop"
quantity=2
price = 499.99
in_stock = True

print("Item:", item_name, ", Qty:", quantity, ", Price:", price, ", Available:", in_stock)

total_cost = quantity * price
print("Total Cost:", total_cost)




