# CARBON SAVINGS CALCULATOR
A simple Flask web application that calculates estimated carbon dioxide (CO2) savings based on user inputs about car usage, fuel type, traffic conditions, and trip details.

---

## Features

- Calculates CO2 savings considering distance, fuel type, traffic, number of riders, idle time, trip time, car age, and air conditioning usage.
- Interactive web UI for easy data input.
- Returns estimated carbon savings in grams of CO2.
- Clean and simple interface styled with custom CSS.

---

## Technologies Used

- *Programming Language:* Python
- *Web Framework:* Flask (a lightweight Python web framework)
- *Frontend:* HTML, CSS, JavaScript (vanilla JS for form submission and API calls)
- *Styling:* Custom CSS for basic styling

---

## Programming Paradigm

This project follows a *procedural and functional programming* style:

- The main logic (carbon savings calculation) is encapsulated in a pure function (calculate_carbon_savings) that takes inputs and returns a result without side effects.
- The Flask app defines routes as functions handling HTTP requests and responses.
- Uses modular design separating backend logic from frontend UI.
- No complex object-oriented patterns; focuses on clarity and simplicity.

---

## How to Run

1. Clone the repository.
2. Make sure you have Python 3 installed.
3. Install Flask if not already installed:

   ```bash
   pip install flask
