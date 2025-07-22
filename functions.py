# Function to calculate average of a list
def calculate_average(values):
    return sum(values) / len(values)

# Function to display carbon data for each city
def display_city_data(city_data):
    print(f"{'City':<12} {'Temp (°C)':<12} {'Carbon (g CO₂)':<16}")
    print("-" * 40)
    for city, temp, carbon in city_data:
        print(f"{city:<12} {temp:<12} {carbon:<16}")

# Main function
def main():
    # Dataset: (City, Temperature, Carbon Footprint)
    data = [
        ("Mumbai", 33.5, 120),
        ("Delhi", 38.2, 180),
        ("Pune", 30.1, 90),
        ("Chennai", 34.3, 110),
        ("Bengaluru", 29.0, 70),
        ("Hyderabad", 35.0, 150),
        ("Kolkata", 36.5, 95)
    ]

    # Extract temperature and carbon values
    temperatures = [entry[1] for entry in data]
    carbon_footprints = [entry[2] for entry in data]

    # Calculate averages
    avg_temp = calculate_average(temperatures)
    avg_carbon = calculate_average(carbon_footprints)

    # Display results
    display_city_data(data)
    print("\nAverage Temperature:", round(avg_temp, 2), "°C")
    print("Average Carbon Footprint:", round(avg_carbon, 2), "g CO₂")

# Run the program
main()
