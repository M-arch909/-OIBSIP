import tkinter as tk
from tkinter import messagebox
import requests
API_KEY = "32d6f6e19ede2c4bce74114846e51115"
def get_weather():
    city = city_entry.get() 
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].title()
        weather_info = (
            f"City: {city}\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Condition: {description}"
        )
        result_label.config(text=weather_info)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")
city_label = tk.Label(root, text="Enter City Name:")
city_label.pack(pady=10)
city_entry = tk.Entry(root, width=20)
city_entry.pack(pady=5)
fetch_button = tk.Button(root, text="Get Weather", command=get_weather)
fetch_button.pack(pady=10)
result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)
root.mainloop()
#Input: Enter City Name: Junagadh