# main_controller.py

import functions
import function_carbonFootprint
import carbon_footprint_average
import carbon_footprint_highestfootprint
import carbon_footprint_threshhold
import lambda_function

def print_separator(title):
    print("\n" + "="*60)
    print(f"{title}")
    print("="*60)

def main():
    print_separator("1. Basic Function Implementation")
    if hasattr(functions, 'main'):
        functions.main()

    print_separator("2. Carbon Footprint from Energy Consumption")
    if hasattr(function_carbonFootprint, 'main'):
        function_carbonFootprint.main()

    print_separator("3. Average Temperature & Carbon Footprint")
    if hasattr(carbon_footprint_average, 'main'):
        carbon_footprint_average.main()

    print_separator("4. Highest Carbon Emitting City")
    if hasattr(carbon_footprint_highestfootprint, 'main'):
        carbon_footprint_highestfootprint.main()

    print_separator("5. Cities Above Carbon Threshold")
    if hasattr(carbon_footprint_threshhold, 'main'):
        carbon_footprint_threshhold.main()

    print_separator("6. Filter Cities Below Sustainability Threshold")
    if hasattr(lambda_function, 'main'):
        lambda_function.main()

if __name__ == "__main__":
    main()
