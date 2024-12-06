import json
expenses=[]
def add_expenses():
    description=input("Enter description:")
    amount=float(input("Enter amount:"))
    category=input("Enter category(e.g,Food,Transport):")
    date=input("Enter date (YY_MM_DD):")

    expense={"description":description,
             "amount":amount,
             "category":category,
             "date":date}
    expenses.append(expense)
    print("expenses added successfully")


def view_expenses():
    if not expenses:
        print("no expenses recorded")
        return
    for i,expense in enumerate(expenses,start=1):
        print(f"{i}.{expense['description']} - {expense['amount']} {expense['category']} on {expense['date']}")


def delete_expenses():
    view_expenses()
    index=int(input("enter the expenses number to delete"))-1
    if 0<=index<len (expenses):
        deleted_expense=expenses.pop(index)
        print(f"deleted:{deleted_expense['description']}")
    else:
        print("invalid selection")
    
def summarize_by_category():
    summary={}
    for expense in expenses:
        category=expense['category']
        summary[category]=summary.get(category,0)+expense["amount"]
    for category,total in summary.items():
        print(f"{category}{total:.2f}")

def calculate_total():
    total=sum(expense['amount']for expense in expenses)
    print(f"total expenses:{total:.2f}")

def save_data():
    with open ("expenses.json","w")as file:
        json.dump(expenses,file)
    print("data saved.")
def load_data():
    global expenses
    try:
        with open("expenses.json","r")as file:
            expenses=json.load(file)
    except FileNotFoundError:
        print("no saved data found")


# main pprogram
def main():
    load_data()
    while True:
        print("\n1.ADD EXPENSE\n2.VIEW EXPENSES\n3.DELETE EXPENSES\n4.SUMMARIZE BY CATEGORY\n5.CALCULATE TOTAL\n6.SAVE&EXIT")
        choice=input("choose an option:")
        if choice=="1":
            add_expenses()
        elif choice=="2":
            view_expenses()
        elif choice=="3":
            delete_expenses()
        elif choice=="4":
            summarize_by_category()
        elif choice=="5":
            calculate_total()
        elif choice=="6":
            save_data()
            print("existing.goodbye!")
        else:
            print("invalid choice.please try again.")

if __name__=="__main__":
    main()
