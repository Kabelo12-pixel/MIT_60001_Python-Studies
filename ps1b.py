annual_salary =float(input("Enter your annual_salary: "))
portion_saved = float(input("Enter the percentage of your salary,you would like to save, as a decimal: "))
total_cost = int(input("What is the total cost of your dream home?: "))
semi_annual_raise = float(input("Enter your semi_annual_raise: "))
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
    if(months>0 and months % 6 ==0):
        monthly_salary += monthly_salary * semi_annual_raise
        monthly_savings += monthly_savings * semi_annual_raise



print(f"Number of months: ",months)
