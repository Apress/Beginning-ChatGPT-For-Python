import requests

def get_weather(api_key, city):
    base_url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {
        "apikey": api_key,
        "q": city,
    }
    response = requests.get(base_url, params=params)
    location_data = response.json()
    if location_data:
        if isinstance(location_data, list) and len(location_data) > 0:
            location_key = location_data[0]["Key"]
            weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}"
            params = {
                "apikey": api_key,
            }
            response = requests.get(weather_url, params=params)
            weather_data = response.json()
            if weather_data:
                weather_text = weather_data[0]["WeatherText"]
                temperature = weather_data[0]["Temperature"]["Metric"]["Value"]
                print(f"The current weather in {city} is {weather_text} with a temperature of {temperature}°C.")
            else:
                print("Weather data not found.")
        else:
            print("No location data found for the provided city.")
    else:
        print("Location not found.")

if __name__ == "__main__":
    api_key = "YOUR-API-KEY-HERE"
    city = input("Enter your city: ")
    get_weather(api_key, city)
