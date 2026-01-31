import numpy as np
import matplotlib.pyplot as plt

# Parameters
R = 1000        # Resistance in ohms
C = 1e-6        # Capacitance in farads
V = 5           # Supply voltage in volts

# Time array
t = np.linspace(0, 0.01, 1000)

# Charging capacitor
Vc_charge = V * (1 - np.exp(-t / (R * C)))

# Discharging capacitor
Vc_discharge = V * np.exp(-t / (R * C))

# Plotting
plt.plot(t, Vc_charge, label="Charging")
plt.plot(t, Vc_discharge, label="Discharging")

plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("RC Circuit Charging and Discharging")
plt.legend()
plt.grid(True)
plt.show()
