import random
import time
import matplotlib.pyplot as plt

temps = []
humidity = []
time_steps = []

try:
    with open("environment_data.csv", "w") as csv_file, open("environment_data.txt", "w") as txt_file:
        csv_file.write("Time,Temperature,Humidity\n")
        txt_file.write("Time Temperature Humidity\n")

        for t in range(10):
            temp = 25 + random.uniform(-1, 1)
            hum = 60 + random.uniform(-5, 5)

            temps.append(temp)
            humidity.append(hum)
            time_steps.append(t)

            csv_file.write(f"{t},{temp},{hum}\n")
            txt_file.write(f"{t} {temp} {hum}\n")

            time.sleep(0.5)

except IOError:
    print("Error: Unable to write to file.")

# Plotting
plt.plot(time_steps, temps, label="Temperature (°C)")
plt.plot(time_steps, humidity, label="Humidity (%)")

plt.xlabel("Time (s)")
plt.ylabel("Values")
plt.title("Temperature and Humidity Data Log")
plt.legend()
plt.grid(True)
plt.show()
