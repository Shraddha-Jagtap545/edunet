
data = [
    ("Mumbai", 33.5, 120),
    ("Delhi", 38.2, 180),
    ("Pune", 30.1, 90),
    ("Chennai", 34.3, 110),
    ("Bengaluru", 29.0, 70),
    ("Hyderabad", 35.0, 150),
    ("Kolkata", 36.5, 95)
]

# Extract carbon footprints to calculate average
carbon_footprints = [entry[2] for entry in data]
average_footprint = sum(carbon_footprints) / len(carbon_footprints)

# Threshold is set as average
threshold = average_footprint

# Find cities with carbon footprint above threshold
above_threshold = [entry for entry in data if entry[2] > threshold]

# Print results
print(f"Average Carbon Footprint: {average_footprint:.2f} g CO₂")
print("\nCities with Carbon Footprint ABOVE Average Threshold:\n")
print(f"{'City':<12} {'Temp (°C)':<12} {'Carbon (g CO₂)':<16}")
print("-" * 40)
for city, temp, carbon in above_threshold:
    print(f"{city:<12} {temp:<12} {carbon:<16}")
