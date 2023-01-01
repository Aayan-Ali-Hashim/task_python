import tkinter as tk
import requests
import json
from PIL import ImageTk, Image

# API key for OpenWeatherMap API
API_KEY = "96ec65475b16bcbf398e52fe900ecd81"

# Function to get weather data for a given city
def get_weather(city):
  # Send an HTTP request to the OpenWeatherMap API
  response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}")

  # Parse the JSON response
  weather_data = json.loads(response.text)

  # Get the current temperature in Celsius
  temperature = weather_data["main"]["temp"] - 273.15
  temperature = round(temperature, 1)

  # Get the weather description
  description = weather_data["weather"][0]["description"]

  # Return the weather data as a string
  return f"Temperature: {temperature}°C\nDescription: {description}"

# Create the main window
window = tk.Tk()
window.iconbitmap(r'C:\Users\eshal\Desktop\webscrape\c1\weather-icon.png')
window.geometry("500x600")
window.title("Weather App")
img = ImageTk.PhotoImage(Image.open(r"C:\Users\eshal\Desktop\webscrape\c1\weather.jpeg"),size=(25,10))  
l=tk.Label(image=img)
l.pack()
# Create a label for the city input
city_label = tk.Label(text="Enter city:",font=("Times",20))
city_label.pack()

# Create a text box for the city input
city_entry = tk.Entry(font=('Times',20))
city_entry.pack()

# Create a button to get the weather
def get_weather_button_click():
  weather_data = get_weather(city_entry.get())
  weather_label.config(text=weather_data)

get_weather_button = tk.Button(text="Enter", command=get_weather_button_click)
get_weather_button.pack()

# Create a label to display the weather data
weather_label = tk.Label(text="The weather : ",font=("Times",17))
weather_label.pack()

# Start the GUI event loop
window.mainloop() 

