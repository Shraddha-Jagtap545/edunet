# List of data: (City, Temperature in °C, Carbon Footprint in grams of CO2)
data = [
    ("Mumbai", 33.5, 120),
    ("Delhi", 38.2, 180),
    ("Pune", 30.1, 90),
    ("Chennai", 34.3, 110),
    ("Bengaluru", 29.0, 70),
    ("Hyderabad", 35.0, 150),
    ("Kolkata", 36.5, 95)
]

# Separate temperature and carbon footprint lists
temperatures = [entry[1] for entry in data]
carbon_footprints = [entry[2] for entry in data]

# Calculate averages
avg_temp = sum(temperatures) / len(temperatures)
avg_carbon = sum(carbon_footprints) / len(carbon_footprints)

# Display results
print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Average Carbon Footprint: {avg_carbon:.2f} g CO₂")
