import requests

def weather_data(query):
   api_key = "ea52a1823fbabd62afcc3189b1bb0d62"
   url = "http://api.openweathermap.org/data/2.5/weather?"
   complete_url = url + query + "&units=imperial" + "&" + "appid=" + api_key 
   response = requests.get(complete_url)
   return response.json()

def display_results(weather,city):
   print("{}'s temperature: {}°F ".format(city,weather['main.temp']))
   print("Wind speed: {} m/s".format(weather['wind.speed']))
   print("Description: {}".format(weather['weather.description']))
   print("Weather: {}".format(weather['weather.main']))

def main():
   city=input("Enter the city:")
   
   try:
      query= 'q=' + city
      w_data = weather_data(query)
      display_results(w_data, city)
      
   except:
      print("City name not found")

if __name__=='__main__':
   main()