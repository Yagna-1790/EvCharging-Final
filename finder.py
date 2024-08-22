import requests

API_URL = "https://api.openchargemap.io/v3/poi/"
API_KEY = "your_open_charge_map_api_key"  # Replace with your API key

def find_ev_stations(lat, lon, distance_km=10):
    params = {
        'latitude': lat,
        'longitude': lon,
        'distance': distance_km,
        'maxresults': 5,
        'compact': 'true',
        'key': API_KEY
    }
    
    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Could not retrieve data")
        return None
