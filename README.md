## Weather Data CLI 
## Project Description
Weather Data CLI is a Python command-line application that retrieves current weather information for a given city using the OpenWeatherMap API.
## Objectives
- Retrieve real-time weather information.
- Integrate a weather API using Python.
- Process JSON responses.
- Handle API errors and invalid city names.
## Technologies Used
- Python
- Requests Library
- OpenWeatherMap API
- JSON
## Features
- Search weather by city name.
- Display temperature in Celsius.
- Display weather conditions.
- Display humidity.
- Display wind speed.
- Handle invalid city names.
- Handle API and network errors.
## Installation
1. Install Python.
2. Install the required library:
pip install requests
3. Get an API key from OpenWeatherMap.
4. Set the API key as an environment variable named "OPENWEATHER_API_KEY".
5. Run the application:
python weather_cli.py
## Sample Output
WELCOME TO WEATHER DATA CLI
Enter city name: Hyderabad
===== WEATHER REPORT =====
City: Hyderabad
Temperature: 28.5 °C
Weather: scattered clouds
Humidity: 65 %
Wind Speed: 3.2 m/s
==========================
## Learning Outcomes
- Understanding API integration.
- Working with JSON data.
- Using Python functions.
- Handling exceptions.
- Processing user input.
## Conclusion
This project demonstrates how Python can retrieve and display real-time weather information through API integration and error handling.
