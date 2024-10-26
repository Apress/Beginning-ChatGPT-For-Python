"""
Script to fetch current weather information using AccuWeather API.
"""

import requests

def get_weather(accuweather_api_key, city):
    """
    Get current weather information for a given city using AccuWeather API.

    Args:
        accuweather_api_key (str): AccuWeather API key.
        city (str): Name of the city for which weather information is requested.

    Returns:
        None
    """
    base_url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {
        "apikey": accuweather_api_key,
        "q": city,
    }
    response = requests.get(base_url, params=params, timeout=10)
    location_data = response.json()
    if location_data:
        location_key = location_data[0]["Key"]
        weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}"
        params = {
            "apikey": accuweather_api_key,
        }
        response = requests.get(weather_url, params=params, timeout=10)
        weather_data = response.json()
        if weather_data:
            weather_text = weather_data[0]["WeatherText"]
            temperature_imperial = weather_data[0]["Temperature"]["Imperial"]["Value"]

            # Fetching icon number and icon URL
            icon_number = weather_data[0]["WeatherIcon"]
            icon_url = (
                f"http://developer.accuweather.com/sites/default/files/"
                f"{icon_number:02d}-s.png"
            )

            # Making API call to get weather headline
            headline_url = (
                f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/"
                f"{location_key}"
            )
            response = requests.get(headline_url, params=params, timeout=10)
            headline_data = response.json()
            if headline_data and "Headline" in headline_data:
                headline_text = headline_data["Headline"]["Text"]
                print(f"The current weather in {city} is {weather_text} "
                      f"with a temperature of {temperature_imperial}°F.")
                print(f"Weather Headline: {headline_text}")
                print(f"Weather Icon: {icon_url}")
            else:
                print("Weather headline not found.")
        else:
            print("Weather data not found.")
    else:
        print("Location not found.")

if __name__ == "__main__":
    ACCUWEATHER_API_KEY = "your-accuweather-api-key-here"
    user_city = input("Enter your city: ")
    get_weather(ACCUWEATHER_API_KEY, user_city)