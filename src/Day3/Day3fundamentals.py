#List and Tuples
number=[10,20,30,40]
cordinates=(5,10)
print(number)
print(cordinates)


#indexing and Slicing
a=[100,200,300,400,500,600,700,800]
print(a)
print(a[:3])
print(a[-3:-1])
print(a[-1:-3])
print(a[1:8:3])
print(a[-3:-1:2])

#list Methods
marks=[85,45,32,44]

marks.append(88)
print(marks)
marks.pop()
print(marks)
marks.sort()
print(marks)
marks.insert(2,88)
print(marks)
marks.remove(88)
print(marks)
marks.reverse()
print(marks)

# Practical Example: Managing an Inventory List
inventory = ["Apples", "Bananas", "Carrots", "Dates"]
print("Current Inventory:", inventory)
inventory.append("Eggs")
print("After adding Eggs:", inventory)
inventory.remove("Bananas")
print("After removing Bananas:", inventory)
inventory.sort()
print("Final Updated Inventory:", inventory)

print("\n")



# Practical Example: Temperature Readings Throughout the Day
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print("First Reading:", temperatures[0])
print("Last Reading:", temperatures[-1])
print("Afternoon Peak Readings:", temperatures[3:6])
print("Last 3 Hours:", temperatures[-3:])

print("\n")


# Tuple Immutability Example
screen_res = (1920, 1080)
print(f"Current Resolution: {screen_res[0]}x{screen_res[1]}")
print("Tuples cannot be modified!")
screen_res[0] = 1280  

