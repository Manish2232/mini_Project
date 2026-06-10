#Expanse tracker Project

expenses_list = [] # list of all expense
print("Welcome to Expense Tracker : My Dear")

while True:
    print("====MENU====")
    print("1. Add Expanse")
    print("2. View All Expanses")
    print("3. View Total Expanse")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice : "))

# Add Expenses
    if(choice == 1):
        date = input("Enter Date of Expense (dd/mm/yy) : ")
        category = input("Enter the Expense Category : ")
        description = input("Expense Descripion : ")
        amount = float(input("Expense Amount : "))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }

        expenses_list.append(expense)
        print("\n Expense is added succesfully")

#2. View All Expenses
    elif(choice == 2):
        if(len(expenses_list) == 0):
            print("No Expense Added.")
        else:
            print("====Your All Expenses====")
            count = 1
            for each_Expense in expenses_list:
                print(f"Expense Number {count} -> {each_Expense["date"]}, {each_Expense["description"]}, {each_Expense["amount"]}")
                count += 1

#3. View Total spending
    elif(choice == 3):
        total = 0
        for each_Expense in expenses_list:
            total += each_Expense["amount"]

        print("\n Total Expanse = ", total)

#4. Exit
    elif(choice == 4):
        print("Thanks! You used this software")
        break

    else:
        print("INVALID CHOICE : Try again")

