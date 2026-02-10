name=input("Enter the Name:")
goal=input("Enter the Goal:")

with open("journal.txt","a")as file:
    file.write(f"{name} {goal}\n")

print("Saved sucessfully")


