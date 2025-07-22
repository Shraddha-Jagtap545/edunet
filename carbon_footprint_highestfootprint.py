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

# Find the city with the highest carbon footprint
highest_city = max(data, key=lambda x: x[2])  # x[2] is the carbon footprint

# Display result
print("City with Highest Carbon Emission:\n")
print(f"City: {highest_city[0]}")
print(f"Temperature: {highest_city[1]} °C")
print(f"Carbon Footprint: {highest_city[2]} g CO₂")
