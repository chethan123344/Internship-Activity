import csv
with open("students.csv","r",encoding="utf-8-sig")as file:
    reader=csv.DictReader(file)
    print("Student who passed:")
    
    for row in reader:
        if row["Status"]=="Pass":
            print(row["Name"])
