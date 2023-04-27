import requests
import json

OPENAQ_API_BASE = "https://api.openaq.org/v1"
CITIES = ["Stockholm", "Oslo", "Helsinki", "Copenhagen"]

def get_city_measurements(city):
    url = f"{OPENAQ_API_BASE}/measurements?city={city}&limit=100"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error fetching data for {city}: {response.status_code}")
        return []

    data = response.json()
    return data["results"]

def fetch_data():
    all_data = {}
    for city in CITIES:
        city_data = get_city_measurements(city)
        all_data[city] = city_data
        print(f"Fetched {len(city_data)} records for {city}")

    with open("data.json", "w") as f:
        json.dump(all_data, f)

if __name__ == "__main__":
    fetch_data()