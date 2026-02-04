student={
    "name":"chethan",
    "age":21,
    "course":"MCA"
    }

print(student["name"])
student["age"]=22
student["city"]="bantwal"
print(student)


#Dictionary

marks={"math":80,"science":75,"english":85}
print(marks.get("math"))
print(marks.get("history",0))
print(marks)

for subject,score in marks.items():
    print(subject,score)


#update marks
marks["math"]=90
    

#remove value
removed_score=marks.pop("english")
print(marks)

#example
purchase={
        "alice":150,
        "bob":200,
        "charlie":300
        }
for name,amount in purchase.items():
    print(f"{name} spent ${amount}")
    

    print("total customers:",len(purchase))
    print("\n")

n=int(input("Enter the number of customers:"))
user_purchases={}
for name,amount in purchases.items():
    print(f"{name} spent ${amount}")

print("total customers:",len(purchases))


print("\n")
#input dictionary from user
n=int(input("Enter number of customers: "))
user_purchases={}

for i in range(n):
    name=input("Enter customer name: ")
    amount=int(input(f"Enter purchase amount for {name}: "))
    user_purchases[name]=amount
    
    print("User Purchase Data:",user_purchases)
top_customer=max(user_purchases,key=user_purchases.get)
print("top spending customer:",top_customer)
min_customer=min(user_purchases,key=user_purchases.get)
print("least spending customer:",min_customer)

print("\n")
#sets & unique collections

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
print(A & B)

print(3 in A)
    

    
