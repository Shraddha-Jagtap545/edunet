# Sample data: (City, Temperature in °C, Carbon Footprint in kg CO₂)
data = [
    ("Mumbai", 33.5, 320),
    ("Delhi", 38.2, 480),
    ("Pune", 30.1, 290),
    ("Chennai", 34.3, 350),
    ("Bengaluru", 29.0, 260),
    ("Hyderabad", 35.0, 410),
    ("Kolkata", 36.5, 390)
]

# Define threshold
sustainability_threshold = 400  # in kg CO2

# Use lambda function to filter sustainable cities
sustainable_cities = list(filter(lambda city: city[2] < sustainability_threshold, data))

# Display results
print("Cities with Carbon Footprint BELOW 400 kg CO₂:\n")
print(f"{'City':<12} {'Temp (°C)':<12} {'Carbon (kg CO₂)':<18}")
print("-" * 42)
for city, temp, carbon in sustainable_cities:
    print(f"{city:<12} {temp:<12} {carbon:<18}")
