import requests
import json
import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")

w= str("Welcome to Kuku Speaks 1.0 created by Vishalakshi")
print(w)
speaker.Speak(w)
speaker.Speak("Please enter the city name to know the weather report")
city=input("Enter the name of the city:\n")


url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey=bYm4dtm6U1aOrr8H9hERYqe8JEDxkpoE"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)



wdic=json.loads(response.text)
y=wdic["data"]['values']["temperature"]
x=wdic["data"]['values']["humidity"]



speaker.Speak(f"the current weather report of {city} consists of: temperature is {y} degree celcius and humidity is {x}%")
speaker.Speak("Hoping for a nice day ahead!")
