import requests

def get_route_info(google_maps_api_key, origin, destination):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={google_maps_api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        route_data = response.json()
        if route_data["status"] == "OK":
            route_info = route_data["routes"][0]["legs"][0]
            distance = route_info["distance"]["text"]
            duration = route_info["duration"]["text"]
            print(f"Distance: {distance}, Duration: {duration}")
        else:
            print("Error:", route_data["status"])
    else:
        print("Error:", response.status_code)

# Replace ‘YOUR_GOOGLE_MAPS_API_KEY’ with your actual Google Maps API key
google_maps_api_key = 'YOUR_GOOGLE_MAPS_API_KEY'
origin = 'New York, NY'  # Example origin
destination = 'Los Angeles, CA'  # Example destination

get_route_info(google_maps_api_key, origin, destination)