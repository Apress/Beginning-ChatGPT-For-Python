import requests
import json

# Define the payload
payload = {
    "origin": {
        "location": {
            "latLng": {
                "latitude": 37.419734,
                "longitude": -122.0827784
            }
        }
    },
    "destination": {
        "location": {
            "latLng": {
                "latitude": 37.417670,
                "longitude": -122.079595
            }
        }
    },
    "travelMode": "DRIVE",
    "routingPreference": "TRAFFIC_AWARE",
    "departureTime": "2025-02-17T17:00:00Z",
    "computeAlternativeRoutes": False,
    "routeModifiers": {
        "avoidTolls": False,
        "avoidHighways": False,
        "avoidFerries": False
    },
    "languageCode": "en-US",
    "units": "IMPERIAL"
}

# Define headers
headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": "your-google-api-key",
    "X-Goog-FieldMask": "routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline"
}

# Make the request
response = requests.post("https://routes.googleapis.com/directions/v2:computeRoutes", json=payload, headers=headers)

# Print the response
print(response.json())
