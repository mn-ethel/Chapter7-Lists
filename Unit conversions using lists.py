
conversion_factors = [12, 1/3, 1/5280, 304.8, 30.48, 0.3048, 0.0003048]
conversion_units = ["Inches", "Yards", "Miles", "Millimeters", "Centimeters", "Meters", "Kilometers"]

feet = float(input("Enter length in feet: "))

print("\nChoose a conversion:")
for i, unit in enumerate(conversion_units, 1):
    print(f"{i}. {unit}")

# Get user choice
choice = int(input("\nEnter your choice (1-7): "))

# Validate input
if 1 <= choice <= len(conversion_factors):
    converted_value = feet * conversion_factors[choice - 1]
    print(f"\n{feet} feet is equal to {converted_value:.4f} {conversion_units[choice - 1]}")
else:
    print("\nInvalid choice! Please enter a number between 1 and 7.")
