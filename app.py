from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_daily_cost(total_monthly_cost, num_people):
    monthly_cost_per_person = total_monthly_cost / num_people
    daily_cost_per_person = monthly_cost_per_person / 30
    return daily_cost_per_person

def calculate_daily_chore_time(total_monthly_time, num_people):
    daily_time_per_person = total_monthly_time / 30 / num_people
    return daily_time_per_person

@app.route('/guide')
def guide():
    return render_template('guide.html')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_data = request.form

        # First set of inputs
        total_monthly_rent1 = int(request.form.get("total_monthly_rent1", 0))
        num_people1 = int(request.form.get("num_people1", 0))
        num_vehicles1 = int(request.form.get("num_vehicles1", 0))
        include_groentetuin1 = 'include_groentetuin1' in request.form
        include_grasgevoerd1 = 'include_grasgevoerd1' in request.form
        include_huisonderhoud1 = 'include_huisonderhoud1' in request.form

        # Second set of inputs
        total_monthly_rent2 = int(request.form.get("total_monthly_rent2", 0))
        num_people2 = int(request.form.get("num_people2", 0))
        num_vehicles2 = int(request.form.get("num_vehicles2", 0))
        include_groentetuin2 = 'include_groentetuin2' in request.form
        include_grasgevoerd2 = 'include_grasgevoerd2' in request.form
        include_huisonderhoud2 = 'include_huisonderhoud2' in request.form

        # Calculations for the first set
        costs1 = {
            'Huur': total_monthly_rent1,
            'Auto': 200 * num_vehicles1,
            'Gas, water, licht': 150 + (40 * num_people1),
            'Internet': 60,
        }
        if include_grasgevoerd1:
            costs1['Eten'] = (600 * num_people1) * (1 - 0.05 * num_people1)
        else:
            costs1['Eten'] = (300 * num_people1) * (1 - 0.05 * num_people1)

        if include_huisonderhoud1:
            costs1['Huis onderhoud'] = 300
        else:
            costs1['Huis onderhoud'] = 0

        chores1 = {
            'Koken, schoonmaak, was': (30 + (10 * num_people1)),
            'Boodschappen doen': 16,
            'Voertuig onderhoud': 4 * num_vehicles1,
        }
        if include_groentetuin1:
            chores1['Groentetuin'] = 60

        daily_costs1 = {key: round(calculate_daily_cost(value, num_people1), 2) for key, value in costs1.items()}
        daily_chores1 = {key: round(calculate_daily_chore_time(value, num_people1), 2) for key, value in chores1.items()}

        total_daily_cost1 = round(sum(daily_costs1.values()), 2)
        total_daily_chore_time1 = round(sum(daily_chores1.values()), 2)
        total_weekly_cost1 = round(total_daily_cost1 * 7, 2)
        total_weekly_chore_time1 = round(total_daily_chore_time1 * 7, 2)

        # Calculations for the second set
        costs2 = {
            'Huur': total_monthly_rent2,
            'Auto': 200 * num_vehicles2,
            'Gas, water, licht': 150 + (40 * num_people2),
            'Internet': 60,
        }
        if include_grasgevoerd2:
            costs2['Eten'] = (600 * num_people2) * (1 - 0.05 * num_people2)
        else:
            costs2['Eten'] = (300 * num_people2) * (1 - 0.05 * num_people2)

        if include_huisonderhoud2:
            costs2['Huis onderhoud'] = 300
        else:
            costs2['Huis onderhoud'] = 0

        chores2 = {
            'Koken, schoonmaak, was': (30 + (10 * num_people2)),
            'Boodschappen doen': 16,
            'Voertuig onderhoud': 4 * num_vehicles2,
        }
        if include_groentetuin2:
            chores2['Groentetuin'] = 60

        daily_costs2 = {key: round(calculate_daily_cost(value, num_people2), 2) for key, value in costs2.items()}
        daily_chores2 = {key: round(calculate_daily_chore_time(value, num_people2), 2) for key, value in chores2.items()}

        total_daily_cost2 = round(sum(daily_costs2.values()), 2)
        total_daily_chore_time2 = round(sum(daily_chores2.values()), 2)
        total_weekly_cost2 = round(total_daily_cost2 * 7, 2)
        total_weekly_chore_time2 = round(total_daily_chore_time2 * 7, 2)

        return render_template("index.html", form_data=form_data,
                               daily_costs1=daily_costs1,
                               daily_chores1=daily_chores1,
                               total_daily_cost1=total_daily_cost1,
                               total_daily_chore_time1=total_daily_chore_time1,
                               total_weekly_cost1=total_weekly_cost1,
                               total_weekly_chore_time1=total_weekly_chore_time1,
                               total_monthly_rent1=total_monthly_rent1,
                               num_people1=num_people1,
                               num_vehicles1=num_vehicles1,
                               include_groentetuin1=include_groentetuin1,
                               include_grasgevoerd1=include_grasgevoerd1,
                               include_huisonderhoud1=include_huisonderhoud1,
                               daily_costs2=daily_costs2,
                               daily_chores2=daily_chores2,
                               total_daily_cost2=total_daily_cost2,
                               total_daily_chore_time2=total_daily_chore_time2,
                               total_weekly_cost2=total_weekly_cost2,
                               total_weekly_chore_time2=total_weekly_chore_time2,
                               total_monthly_rent2=total_monthly_rent2,
                               num_people2=num_people2,
                               num_vehicles2=num_vehicles2,
                               include_groentetuin2=include_groentetuin2,
                               include_grasgevoerd2=include_grasgevoerd2,
                               include_huisonderhoud2=include_huisonderhoud2)
    
    # Default form values
    return render_template("index.html", form_data={},
                            daily_costs1={},
                           daily_chores1={},
                           total_daily_cost1=0,
                           total_daily_chore_time1=0,
                           total_weekly_cost1=0,
                           total_weekly_chore_time1=0,
                           daily_costs2={},
                           daily_chores2={},
                           total_daily_cost2=0,
                           total_daily_chore_time2=0,
                           total_weekly_cost2=0,
                           total_weekly_chore_time2=0,
                           total_monthly_rent1=0,
                           num_people1=0,
                           num_vehicles1=0,
                           include_groentetuin1=False,
                           include_grasgevoerd1=False,
                           include_huisonderhoud1=False,
                           total_monthly_rent2=0,
                           num_people2=0,
                           num_vehicles2=0,
                           include_groentetuin2=False,
                           include_grasgevoerd2=False,
                           include_huisonderhoud2=False)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1100)
