
import requests# enables the program to make http requests

class WeatherApp:
    def __init__(self, API_KEY="9d754d70a3a94628b76195009252010"):#initialises the api key that is unique to my account to make requests
        self.API_KEY = API_KEY

    def weather(self):
        CITY = input("Please enter the name of your city: ").strip().title()#removes trailing spaces and capitalises each word

        print(f"You have chosen: {CITY}")#tells the user their input
        url = f"http://api.weatherapi.com/v1/current.json?key={self.API_KEY}&q={CITY}&aqi=no"#the url that follows the documentation of weatherAPI.com
        response = requests.get(url)

        if response.status_code == 200:#if the response code is 200, which measn successful the code will run as normal
            
            data = response.json()
            location = data["location"]["name"]
            country = data["location"]["country"]
            temp_c = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            humidity = data["current"]["humidity"]
            wind_kph = data["current"]["wind_kph"]
            database=(location,country,temp_c,condition,humidity,wind_kph)
            print(f"🌤️ Weather in {location}, {country}:")
            print(f"Temperature: {temp_c}°C")
            print(f"Condition: {condition}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_kph} kph \n")
            choice=input("would you like to save this infor for use in your notepad?")
            if 'n' in choice:
                print("ok, have a nice day")
                return None
            if "ye" in choice:
                print("saving info...")
                return database
        else:#otherwise the request will fail if it receives 400-500 or any other code
            print("API request failed: error — no valid location found")


