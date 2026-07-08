annual_salary =float(input("Enter your annual_salary: "))
portion_saved = float(input("Enter the percentage of your salary,you would like to save, as a decimal: "))
total_cost = int(input("What is the total cost of your dream home?: "))
portion_down_payment = 0.25
target_savings= total_cost*portion_down_payment



rate_of_return = 0.04
current_savings = 0
invested_amount = current_savings*rate_of_return/12
monthly_salary = annual_salary/12
monthly_savings = monthly_salary*portion_saved
months = 0

while current_savings<target_savings:
    current_savings += current_savings * (rate_of_return/12)
    current_savings += monthly_savings
    months += 1
print(f"Number of months: ",months)

