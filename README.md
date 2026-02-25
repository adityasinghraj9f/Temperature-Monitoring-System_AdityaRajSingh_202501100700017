# Temperature-Monitoring-System_AdityaRajSingh_202501100700017
**Problem Statement**
- Build a Python program to display messages according to the temperature received from an assumed IoT system.
- Accept maximum and minimum temperature limits from the user.
- Generate random temperature values at 2-second intervals.
- Compare the generated values with the limits and display appropriate messages.

**Approach**
- Input Handling:
- The program prompts the user to enter minimum and maximum temperature limits.
- Random Temperature Generation:
- Uses Python’s random.uniform() to simulate IoT sensor readings.
- Generates values slightly beyond the given limits to test alert conditions.
- Comparison Logic:
- If temperature < min → Display Low Temperature Alert.
- If temperature > max → Display High Temperature Alert.
- Else → Display Safe Range Message.
- Loop & Delay:
- Runs continuously in a while True loop.
- Uses time.sleep(2) to simulate real-time monitoring at 2-second intervals.

**Sample Output**

Enter minimum temperature limit: 20
Enter maximum temperature limit: 30

Starting IoT temperature monitoring...

Current Temperature: 18.45 °C
⚠️ Alert: Temperature is below the minimum limit!

Current Temperature: 25.67 °C
✅ Temperature is within the safe range.

Current Temperature: 32.10 °C
⚠️ Alert: Temperature is above the maximum limit!
