import json

# Load user data from user.json
with open('file.json', 'r') as file:
    data = json.load(file)

print("Type 'user' to enter your salary and expenses manually.")
print("Type 'file' to calculate savings for all users from file.\n")

choice = input("Enter your choice: ")

if choice == "user":
    salary = int(input("Enter your salary: "))
    expenses = 0
    n = int(input("How many expenses do you want to add? "))

    for i in range(n):
        category = input("Enter expense name: ")
        amount = int(input("Enter amount for " + category + ": "))
        expenses += amount

    print("Total saved amount is : ", salary - expenses)

elif choice == "file":
    for user in data:
        name = user["Name"]
        salary = user["salary"]
        expenses = user["Electricity"] + user["Internet"] + user["Groceries"] + user["Entertainment"] + user["EMI"]
        saved = salary - expenses
        print(name, "saved ₹", saved)

else:
    print("Invalid choice. Please enter 'user' or 'file'.")
