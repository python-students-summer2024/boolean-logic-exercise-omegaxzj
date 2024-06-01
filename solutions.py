def is_sweltering():
    temperature = float(input("Enter the current temperature in Fahrenheit: "))
    return temperature > 90

def is_warm():
    temperature = float(input("Enter the current temperature in Fahrenheit: "))
    return 75 <= temperature <= 87

def is_humid():
    humidity_response = input("Is it humid today? (yes/no): ").lower()
    return humidity_response == "yes"

def is_inclement():
    weather_forecast = input("What is the weather forecast today? ").lower()
    return "rain" in weather_forecast or "snow" in weather_forecast or "sleet" in weather_forecast

def is_typical_new_york_summer():
    return is_sweltering() and is_humid()

def is_cool_and_nice():
    return not (is_sweltering() or is_warm() or is_humid() or is_inclement())
