"""Write a program that will determine weather when the value of temperature and humidity is provided by the user.
      TEMPERATURE(C)                   HUMIDITY(%)         WEATHER

      >= 30                            >=90                Hot and Humid
      >= 30                            < 90                Hot
      <30                              >= 90               Cool and Humid
      <30                              <90                 Cool
"""

temperature = int(input("Enter temperature "))
humidity = int(input("Enter humidity "))

def weather(temperature,humidity):
    if temperature>=30 and humidity >=90:
        return ("hot and humid")
    elif temperature>=30 and humidity<90:
        return "Hot"
    elif temperature<30 and humidity>=90:
        return "Cool and humid"
    else:
        return("cool")

print(weather(temperature,humidity))