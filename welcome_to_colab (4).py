# Ohm's Law Calculator with Power

voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (Ohms): "))

if resistance != 0:
    current = voltage / resistance
    power = voltage * current   # P = V * I

    print("Current (A):", current)
    print("Power (W):", power)
else:
    print("Error: Resistance cannot be zero")