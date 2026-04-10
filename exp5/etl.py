import requests
import statistics

# CONFIGURATION
INPUT_CHANNEL_ID = "3318318"
READ_API_KEY = "V67967F4GJ91B08B"
WRITE_API_KEY = "V67967F4GJ91B08B"

INPUT_URL = f"https://api.thingspeak.com/channels/{INPUT_CHANNEL_ID}/fields/1.json"
UPDATE_URL = "https://api.thingspeak.com/update"

def extract_data():
    params = {
        "api_key": READ_API_KEY,
        "results": 25
    }
    try:
        response = requests.get(INPUT_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        feeds = data.get("feeds", [])
        values = [
            float(feed["field1"])
            for feed in feeds
            if feed.get("field1") is not None
        ]
        
        print("Extracted Data:", values)
        return values
    except Exception as e:
        print("Error fetching data:", e)
        return None

def transform_data(data):
    if not data:
        return None, None, None
        
    mean_value = statistics.mean(data)
    median_value = statistics.median(data)
    mode_list = statistics.multimode(data)
    
    # If only one mode → take value, else join as string
    mode_value = mode_list[0] if len(mode_list) == 1 else ",".join(map(str, mode_list))
    
    print("Mean:", mean_value)
    print("Median:", median_value)
    print("Mode:", mode_value)
    
    return mean_value, median_value, mode_value

def load_data(mean_value, median_value, mode_value):
    if mean_value is None:
        print("No data to send")
        return
        
    payload = {
        "api_key": WRITE_API_KEY,
        "field3": round(mean_value, 2),
        "field4": round(median_value, 2),
        "field5": mode_value
    }
    try:
        response = requests.post(UPDATE_URL, data=payload)
        response.raise_for_status()
        print("Data successfully sent to ThingSpeak!")
    except Exception as e:
        print("Error sending data:", e)

def main():
    print("Starting ETL process...")
    raw_data = extract_data()
    
    mean_value, median_value, mode_value = transform_data(raw_data)
    
    load_data(mean_value, median_value, mode_value)
    print("ETL process completed.")

if __name__ == "__main__":
    main()