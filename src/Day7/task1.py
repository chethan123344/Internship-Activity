name=input("Enter the Name:")
goal=input("Enter the Goal:")

with open("journal.txt","a")as file:
    file.write(f"{name} {goal}\n")

print("Saved sucessfully")

#task2
import csv
with open("students.csv","r")as file:
    reader=csv.reader(file)
    
    
    for row in reader:
        if row["Status"]=="pass":
            print(row["Name"])
