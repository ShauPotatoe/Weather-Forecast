import requests

#This function is used to build the site we are going to get the weather information from.
def weather_data(query):
   api_key = "ea52a1823fbabd62afcc3189b1bb0d62"
   url = "http://api.openweathermap.org/data/2.5/weather?"
   complete_url = url + query + "&units=imperial" + "&" + "appid=" + api_key 
   print(complete_url+"\nCity or zipcode was found\n")#To display the website and to show that the city or zipcode was found
   response = requests.get(complete_url)
   return response.json()

#This is to display the current weather of that city or zipcode
#It displays temperature, wind speed, a description of the weather, what it looks like outside, and the humiditiy
def display_results(weather,city):

   print("\n{}'s temperature: {}°F ".format(city,weather['main']['temp']))
   print("Wind speed: {} m/s".format(weather['wind']['speed']))
   print("Description: {}".format(weather['weather'][0]['description']))
   print("Weather: {}".format(weather['weather'][0]['main']))
   print("Humidity: {}%\n".format(weather['main']['humidity']))

#This is the main function. It asks for city or zipcode in order to finish building the url.
def main():
     while True:
          choice =int(input("Enter 1 for City, 2 zip code or 3 to exit:"))#I decided to go this route to give the user a 
                                                                            #decision of either a city or a zip code. 
                                                                          #It also provides a way to exit to the program.

          if choice == 1:
               try:
                   city=input("Enter city name:\n")
                   query= 'q=' + city
                   w_data = weather_data(query)
                   display_results(w_data, city)
      
               except:
                    print("City name not found")
          elif choice == 2:
               try:
                    zipCode=input("Enter Zip code")
                    query= 'zip=' + zipCode
                    w_data = weather_data(query)
                    display_results(w_data, zipCode)
      
               except:
                    print("Zip code not found")
          elif choice == 3:

               break
          else:
               print("Invalid Choice...")

#This is used to call the main method
if __name__=='__main__':
   main()
#Refrences:
#Matthes, E. (2019). Python crash course: A hands-on, project-based introduction to programming (2nd ed.). No Starch Press. 

#OpenWeatherMap.org. (n.d.). Current weather data. OpenWeatherMap. Retrieved March 4, 2022, from https://openweathermap.org/current#format 


