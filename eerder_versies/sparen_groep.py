# Ask the user for daily costs and earnings
daily_costs = float(input("Enter your daily costs: "))
weekly_earnings = float(input("Enter your weekly earnings: "))

# Calculate daily savings
daily_savings = (weekly_earnings / 7) - daily_costs
print(f"Your daily savings are: {daily_savings:.2f}")

# Calculate weekly savings
weekly_savings = daily_savings * 7
print(f"Your weekly savings are: {weekly_savings:.2f}")

# Calculate monthly savings (assuming 30 days in a month)
monthly_savings = daily_savings * 30
print(f"Your monthly savings are: {monthly_savings:.2f}")

# Calculate yearly savings (assuming 365 days in a year)
yearly_savings = daily_savings * 365
print(f"Your yearly savings are: {yearly_savings:.2f}")