import urllib.request
import urllib.parse
import json

API_KEY = "YOUR_API_KEY"

def get_weather(city):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    full_url = url + "?" + urllib.parse.urlencode(params)

    try:
        with urllib.request.urlopen(full_url, timeout=10) as response:
            data = json.loads(response.read().decode())

        print("\n===== WEATHER REPORT =====")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Weather:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"], "%")
        print("Wind Speed:", data["wind"]["speed"], "m/s")
        print("==========================")

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Error: City not found!")
        elif e.code == 401:
            print("Error: Invalid API key!")
        elif e.code == 429:
            print("Error: API rate limit exceeded!")
        else:
            print("API Error:", e.code)

    except urllib.error.URLError:
        print("Error: Check your internet connection.")

    except (KeyError, ValueError):
        print("Error: Invalid weather data.")

    except TimeoutError:
        print("Error: Request timed out.")


def main():
    print("WELCOME TO WEATHER DATA CLI")

    city = input("Enter city name: ").strip()

    if city:
        get_weather(city)
    else:
        print("Please enter a city name.")


if __name__ == "__main__":
    main()
