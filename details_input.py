name = input("Enter your name: ")
weight_kg = float(input("Enter your weight in kilograms (kg): "))
height_m = float(input("Enter your height in meters (m): "))



answer = input(f"Would you like to see your details, {name}? ")
if answer == "yes":
    print(f"Name: {name}")
    print(f'height: {height_m} m')
    print(f"Weight: {weight_kg} kg")
else:
 print('  ')