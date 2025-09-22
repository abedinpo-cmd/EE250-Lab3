import requests
import json

# WeatherAPI key
WEATHER_API_KEY = '044649b2cc6246c9abd05831252209'  # TODO: Replace with your own WeatherAPI key (Done)

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    base_url = "http://api.weatherapi.com/v1/current.json"
    url = f"{base_url}?key={WEATHER_API_KEY}&q={city}&aqi=no"


    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    
    response = requests.get(url)

    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.

    url2 = "https://official-joke-api.appspot.com/random_joke"
    res2 = requests.get(url2)
    data2 = res2.json()
    setup = data2['setup']
    punchline = data2['punchline']
    print("JOKE OF THE DAY")
    print(f"{setup}")
    print(f"{punchline}")
    
    if response.status_code == 200:
        # TODO: Parse the JSON data returned by the API. Extract and process the following information:
        # - Current temperature in Fahrenheit
        # - The "feels like" temperature
        # - Weather condition (e.g., sunny, cloudy, rainy)
        # - Humidity percentage
        # - Wind speed and direction
        # - Atmospheric pressure in mb
        # - UV Index value
        # - Cloud cover percentage
        # - Visibility in miles
        data = response.json()
        location = data['location']['name']
        current = data['current']
        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"Weather data for {city}...")
        temp_fahrenheit = current['temp_f']
        feels_temp = current['feelslike_f']
        weather_cond = current['condition']['text']
        humidity = current['humidity']
        wind_mph = current['wind_mph']
        wind_dir = current['wind_dir']
        pressure_mb = current['pressure_mb']
        uv = current['uv']
        cloud = current['cloud']
        vis_miles = current['vis_miles']

        print(f"Temp in fahrenheit: {temp_fahrenheit} *F")
        print(f"Feels like: {feels_temp} *F")
        print(f"Weather condition: {weather_cond}") 
        print(f"Humidity %: {humidity}%")
        print(f"Wind speed: {wind_mph} mph")
        print(f"Wind Direction: {wind_dir}")
        print(f"Atmospheric pressure: {pressure_mb} mb")
        print(f"UV index: {uv}")
        print(f"Cloud coverage: {cloud}%")
        print(f"Miles of visibility: {vis_miles} miles")

        



    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        print(f"Error: {response.status_code}. Something went wrong.")
        if (response.status.code == 400):
            print("ERROR 400: BAD REQUEST. NO PROCESS DUE TO CLIENT ERROR")
        elif (response.status.code == 401): 
            print("ERROR 401: UNAUTHORIZED. CHECK API KEY")
        elif (response.status.code == 403):
            print("ERROR 403: FORBIDDEN REQUEST.")
        elif (response.status.code == 404):
            print("ERROR 404: REQUESTED CITY NOT FOUND")

if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    city = input("Enter City Name: ").strip()
    # TODO: Call the 'get_weather' function with the city name provided by the user.
    get_weather(city)
    pass
