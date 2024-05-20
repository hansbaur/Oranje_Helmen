def calculate_daily_cost(total_monthly_cost, num_people):
    # Calculate the monthly cost per person
    monthly_cost_per_person = total_monthly_cost / num_people

    # Calculate the daily cost per person (assuming 30 days in a month)
    daily_cost_per_person = monthly_cost_per_person / 30

    return daily_cost_per_person

# Test the function
total_monthly_rent = int(input("Huurbedrag: "))
num_people = int(input("Aantal man: "))
num_vehicles = int(input("Aantal voertugen: "))




daily_rent = calculate_daily_cost(total_monthly_rent, num_people)
print(f"De huur per persoon per nacht = {daily_rent:.2f} p/d")


# Calculate car costs
total_monthly_car_cost = (200 * num_vehicles)
daily_car_cost = calculate_daily_cost(total_monthly_car_cost, num_people)
print(f"Autokosten(200/auto/maand) = {daily_car_cost:.2f} p/d")

# Calculate food costs
total_monthly_food_cost = (600 * num_people)
daily_food_cost = calculate_daily_cost(total_monthly_food_cost, num_people)
print(f"Grasgevoerd vlees(600/man/maand) = {daily_food_cost:.2f} p/d")

# Calculate gas, water en licht
total_monthly_gwl_cost = (150 * num_people)
daily_gwl_cost = calculate_daily_cost(total_monthly_gwl_cost, num_people)
print(f"Gas, water, licht(150/man/maand) = {daily_gwl_cost:.2f} p/d")

# Calculate internet costs
total_monthly_internet_cost = (60)
daily_internet_cost = calculate_daily_cost(total_monthly_internet_cost, num_people)
print(f"Internet standaard(60/maand) = {daily_internet_cost:.2f} p/d")


# Calculate time spent on the garden
maandelijkse_tuin_tijd = (60)
Dagelijkse_tuin_tijd = calculate_daily_cost(maandelijkse_tuin_tijd, num_people)
print(f"Tijd in de tuin(15uur/week) = {Dagelijkse_tuin_tijd:.2f}u p/d")






print()

# Calculate total daily cost
total_daily_cost = daily_rent + daily_food_cost + daily_internet_cost + daily_car_cost + daily_gwl_cost
print(f"Totale dagelijkse kosten per man: {total_daily_cost:.2f}")

print()
# Calculate total weekly cost
total_weekly_cost = total_daily_cost * 7
print(f"Totale wekelijkse kosten per man: {total_weekly_cost:.2f}")