
contacts={
    "chethan":"7483062171",
    "yashwith":"9880827169",
    "chidhesh":"9448755593"
}
contacts["srujan"]="9808217369"
contacts["jeevan"]="7483217106"

get_number1=contacts.get("shamanth","contact not found")
get_number2=contacts.get("rakshith","contact not found")

print("-----digital -------")
for name,phone in contacts.items():
    print(f"contact:{name},phone:{phone}")

print(f"Searching for number1:{get_number1}")
print(f"Searching for number1:{get_number2}")


#task2
print("Task 2")
raw_log=["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users=set(raw_log)
is_present="ID05" in unique_users
print(f"Is 'ID05' presented in unique name? {is_present}")

print(f"Is original list length: {len(raw_log)}")
print(f"unique set  length: {len(unique_users)}")
print(f"unique user id: {len(unique_users)}")






#task3
print("task 3")
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

Common_interests=friend_a & friend_b
All_interests=friend_a | friend_b
only_friends_a=friend_a - friend_b

print(f"same interest:{Common_interests}")
print(f"all interest:{All_interests}")
print(f"unique interest:{only_friends_a}")
