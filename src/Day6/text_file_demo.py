file = open("sample.txt", "w")
file.write("Hello, this is a file handling example.")
file.close()

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()


#context manager with open()

with open("Sample.txt","r")as file:
    content=file.read()
    print(content)

#Error handling with try/except
try:
    with open("missing.txt","r")as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist")



#CSV file
import csv
with open("Data.csv","r")as file:
    reader=csv.reader(file)
    
    
    for row in reader:
        print(row[0],row[1],row[2])


# Reading Excel file with openpyxl
import openpyxl
workbook = openpyxl.load_workbook("data1.xlsx")
sheet = workbook.active
for row in sheet.iter_rows(values_only=True):
    print(row[0],row[1],row[2])



    