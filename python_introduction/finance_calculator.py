monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your monthly expenses:"))
savings = monthly_income - monthly_expenses
Projected_Savings = savings * 12 + (savings * 12 * 0.05)
print("Your monthly savings are", savings)
print("Projected savings after one year, with interest, is: ",Projected_Savings)