import csv
import re 
from datetime import datetime
from collections import defaultdict


class Expense():
    def __init__(self,expense_id,description,amount,date):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.date = date

class ExpenseTracker():
    def __init__(self):
        self.expenses = []
        self.next_id = 1

    def add_expense(self,description,amount,date):
        expense = Expense(self.next_id,description,amount,date)
        self.expenses.append(expense)
        self.next_id += 1
        print(f"\nAdded Expense : {description}\nAmount : {amount}\nDate : {date} \n")

    def view_expense(self):
        if not self.expenses:
            print("\nNo Expenses Available.")
        else:
            for expense in self.expenses:
                print (f"\nExpense Id : {expense.expense_id}\nDescription : {expense.description}\nAmount : {expense.amount}\nDate : {expense.date}\n")

    def delete_expense(self,expense_id):
        expense_to_delete = None
        for expense in self.expenses:
            if str(expense.expense_id) == str(expense_id):
                expense_to_delete = expense
                break
        if expense_to_delete:
            self.expenses.remove(expense_to_delete)
            print(f"\nDeleted Expense_id  : {expense_to_delete.expense_id}\nDescription : {expense_to_delete.description}\nAmount : {expense_to_delete.amount}\nDate : {expense_to_delete.date}\n") 
        else:
            print("\nexpense not found 404...\n")
    
    def generate_monthly_report(self):
        if not self.expenses:
            print("No expenses to cummalate Montly Report 404 :(\n")
            return 
        
        report = defaultdict(float)
        for expense in self.expenses:
            month = expense.date[:7]
            report[month] += expense.amount 
        
        print('\nMonthly Expense Report:')
        for month , total in report.items():
            print(f"{month} : {total}")

    def save_to_csv(self,path):
        with open (path,'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID','Description','Amount','Date']) 
            for expense in self.expenses:
                writer.writerow([expense.expense_id,expense.description,expense.amount,expense.date])

        print(f"Saved Expenses to {path} :)")
    

def main():
    tracker = ExpenseTracker()
    print("\n*********** WELECOME TO EXPENSE TRACKER APPLICATION ***********\n")
    while True:
        print("1.ADD EXPENSE \n")
        print("2.VIEW EXPENSE \n")
        print("3.DELETE EXPENSE \n")
        print("4.GENERATE MONTHLY EXPENSE \n")
        print("5.SAVE AND EXIT \n")
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            pattern = r"^[0-9]{4}\-[0-9]{2}\-[0-9]{2}$"
            description = input ("Enter Expense Description: ")
            amount = float(input("Enter Amount: "))
            while True:
                date = input("Enter date (YYYY-MM-DD): ")
                if matches := re.search(pattern,date):
                    break 
                else:
                    print("Please Enter Date in correct format\n")
                    continue
            tracker.add_expense(description,amount,date)
        elif choice == 2:
            tracker.view_expense()
        elif choice == 3:
            expense_to_del = int(input("Enter the Expense Id to delete: \n"))
            tracker.delete_expense(expense_to_del)
        elif choice == 4:
            tracker.generate_monthly_report()
        elif choice == 5:
            tracker.save_to_csv('expenses.csv')
            break
        else:
            print("Invalid Choice, Try again ...\n")
    
if __name__ == '__main__':
    main()



    


