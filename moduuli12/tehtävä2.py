import requests

def get_weather(api_key, lat, lon, exclude=None):
    base_url = "http://api.openweathermap.org/data/3.0/onecall"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key
    }
    if exclude:
        params["exclude"] = exclude
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def get_coordinates(api_key, city, state_code=None, country_code=None, limit=1):
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": f"{city},{state_code},{country_code}",
        "limit": limit,
        "appid": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if not data:
        print(f"Error: No data available for {city}")
        return None, None
    return data[0]['lat'], data[0]['lon']

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def print_weather_data(weather_data):
    print(f"Location: {weather_data['lat']}, {weather_data['lon']}")
    print(f"Timezone: {weather_data['timezone']}")
    print(f"Current weather: {weather_data['current']['weather'][0]['description']}")
    print(f"Current temperature: {kelvin_to_celsius(weather_data['current']['temp'])} degrees Celsius")

def main():
    api_key = "supersecretAPiKey" #use your own apikey you monkey >:[
    city = input("Enter the name of a municipality: ")
    lat, lon = get_coordinates(api_key, city)
    if lat and lon:
        weather_data = get_weather(api_key, lat, lon)
        print_weather_data(weather_data)
    else:
        print("Unable to get weather data.")

if __name__ == "__main__":
    main()

# hv api