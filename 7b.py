import time
import random
def read_sensor():
    """Simulate real time power consumption readings (in watts)"""
    return random.uniform(100, 2000)  # Random power consumption
def process_data(power_usage):
    """Apply filtering and detect abnormal power usage"""
    threshold = 1500  # Set a high-power threshold
    if power_usage > threshold:
        print(f"ALERT: High power usage detected! ({power_usage:.2f} W)")
        return "ALERT"
    else:
        print(f"Normal Power Usage: {power_usage:.2f} W")
        return "Normal"
def main():
    """Main loop to continuously monitor and process sensor data."""
    while True:
        power_usage = read_sensor()  # Read sensor data
        status = process_data(power_usage)  # Process data
        # Send only ALERT data to cloud
        if status == "ALERT":
            print("Sending data to the cloud...")
        time.sleep(5)  # Wait 5 seconds
if __name__ == "__main__":
    main()
