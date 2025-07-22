# Function to calculate carbon footprint
def calculate_carbon_footprint(energy_kwh, emission_factor):
    """
    Calculates the carbon footprint.
    
    Parameters:
    - energy_kwh (float): Energy consumption in kilowatt-hours
    - emission_factor (float): Emission factor in kg CO2 per kWh
    
    Returns:
    - carbon_footprint (float): Resulting carbon footprint in kg CO2
    """
    carbon_footprint = energy_kwh * emission_factor
    return carbon_footprint

# Example usage
def main():
    # Sample values
    energy_used = 350.0  # in kWh
    emission_factor = 0.85  # kg CO2 per kWh (can vary by country)

    # Calculate carbon footprint
    carbon = calculate_carbon_footprint(energy_used, emission_factor)

    # Print result
    print(f"Energy Consumption: {energy_used} kWh")
    print(f"Emission Factor: {emission_factor} kg CO₂/kWh")
    print(f"Carbon Footprint: {carbon:.2f} kg CO₂")

# Run the program
main()
