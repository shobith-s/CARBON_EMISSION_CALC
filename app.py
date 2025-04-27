from flask import Flask, request, jsonify, render_template

app = Flask(_name_)

def calculate_carbon_savings(distance, fuel_type, traffic_condition, num_riders, idle_time, trip_time, car_age, ac_used):
    base_emission = 251
    fuel_adjustment = 1.0
    traffic_adjustment = 1.0
    idle_emissions = float(idle_time) * 10

    distance = float(distance)
    num_riders = int(num_riders)
    trip_time = int(trip_time)
    car_age = int(car_age)

    if fuel_type == 'Diesel':
        fuel_adjustment = 1.15
    elif fuel_type == 'Petrol':
        fuel_adjustment = 1.0
    elif fuel_type == 'EV':
        fuel_adjustment = 0.0

    if traffic_condition == 'Light':
        traffic_adjustment = 1.0
    elif traffic_condition == 'Moderate':
        traffic_adjustment = 1.10
    elif traffic_condition == 'Heavy':
        traffic_adjustment = 1.20

    if 20 <= trip_time or trip_time < 6:
        traffic_adjustment *= 0.95

    if car_age > 5:
        age_adjustment = 1.10
    else:
        age_adjustment = 1.05

    ac_adjustment = 1.10 if ac_used else 1.0

    emissions_per_ride = distance * base_emission * fuel_adjustment * traffic_adjustment * age_adjustment * ac_adjustment
    savings = emissions_per_ride * (1 - 1/num_riders)
    co2_savings = savings + idle_emissions

    return co2_savings

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_savings', methods=['POST'])
def calculate_savings():
    data = request.json

    distance = data['distance']
    fuel_type = data['fuel_type']
    traffic_condition = data['traffic_condition']
    num_riders = data['num_riders']
    idle_time = data['idle_time']
    trip_time = data['trip_time']
    car_age = data['car_age']
    ac_used = data['ac_used']

    savings = calculate_carbon_savings(distance, fuel_type, traffic_condition, num_riders, idle_time, trip_time, car_age, ac_used)

    return jsonify({'carbon_savings': round(savings, 2)})

if _name_ == '_main_':
    app.run(debug=True)