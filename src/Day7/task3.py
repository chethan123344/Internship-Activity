filename=input("Enter the file name:")

try:
    with open(filename,"r")as file:
        content=file.read()
        print("\nFile content:\n")
        print(content)
except FileNotFoundError:
    print("File doesn't exist yet")