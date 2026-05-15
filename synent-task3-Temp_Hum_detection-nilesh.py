import requests
api_key ="5996c1ba85916d833c64030319a87fbd"

city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

code = str(data.get("cod"))

if code == "200":
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")

elif code == "401":
    print("Invalid API key! Please check your API key.")

elif code == "404":
    print("City not found! Please check spelling.")

else:
    print("Error:", data.get("message", "Something went wrong"))
