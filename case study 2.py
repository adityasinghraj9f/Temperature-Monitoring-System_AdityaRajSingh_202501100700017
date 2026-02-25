import random
import time
min = float(input("Enter the minimum value: "))
max = float(input("Enter the maximum value: "))
while True:
  current_temp = random.uniform(0,100)
  print(f"current temperature: {current_temp:.2f}°C")
  if current_temp > max:
    print("Temperature is greater than maximum")
  elif current_temp < min:
    print("Temperature is less than minimum")
  else:
    print("Temperature is within range")
    time.sleep(2)
