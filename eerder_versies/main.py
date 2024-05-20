def calculate_daily_cost(total_monthly_cost, num_people):
    # Calculate the monthly cost per person
    monthly_cost_per_person = total_monthly_cost / num_people
    # Calculate the daily cost per person (assuming 30 days in a month)
    daily_cost_per_person = monthly_cost_per_person / 30
    return daily_cost_per_person

def calculate_daily_chore_time(total_monthly_time, num_people):
    # Calculate the daily time per person (assuming 30 days in a month)
    daily_time_per_person = total_monthly_time / 30 / num_people
    return daily_time_per_person

def main():
    DAYS_IN_MONTH = 30

    # Input values
    total_monthly_rent = int(input("Huurbedrag: "))
    num_people = int(input("Aantal man: "))
    num_vehicles = int(input("Aantal voertuigen: "))

    # Dictionary to store different cost categories and their monthly costs
    costs = {
        'Huur': total_monthly_rent,
        'Auto': 200 * num_vehicles,
        'Eten': 600 * num_people,
        'Gas, water, licht': 150 * num_people,
        'Internet': 60,
    }

    # Dictionary to store different chores and their monthly time commitment
    chores = {
        'Groentetuin': 60,
        'Koken, schoonmaak, was': (30 + (10 * num_people)),
        'Boodschappen doen': 16,
        'Voertuig onderhoud': 4 * num_vehicles,
    }

    # Calculate daily costs per person for each category
    daily_costs = {key: calculate_daily_cost(value, num_people) for key, value in costs.items()}

    # Print daily costs
    print("Dagelijkse kosten per persoon:")
    for category, daily_cost in daily_costs.items():
        print(f"{category} = €{daily_cost:.2f} p/d")

    # Calculate daily chore time per person for each category
    daily_chores = {key: calculate_daily_chore_time(value, num_people) for key, value in chores.items()}

    # Print daily chore times
    print("\nDagelijkse klusjes tijd per persoon:")
    for category, daily_time in daily_chores.items():
        print(f"{category} = {daily_time:.2f}u p/d")

    print()

    # Calculate total daily cost
    total_daily_cost = sum(daily_costs.values())
    print(f"Totale dagelijkse kosten per man: €{total_daily_cost:.2f}")

    # Calculate total daily chore time
    total_daily_chore_time = sum(daily_chores.values())
    print(f"Totale dagelijkse klusjes tijd per man: {total_daily_chore_time:.2f} uur")

    print()

    # Calculate total weekly cost
    total_weekly_cost = total_daily_cost * 7
    print(f"Totale wekelijkse kosten per man: €{total_weekly_cost:.2f}")

    # Calculate total weekly chore time
    total_weekly_chore_time = total_daily_chore_time * 7
    print(f"Totale wekelijkse klusjes tijd per man: {total_weekly_chore_time:.2f} uur")

if __name__ == "__main__":
    main()