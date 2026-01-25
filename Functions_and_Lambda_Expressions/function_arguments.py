#Function Arguments

#Positional Arguments

def display_weather(temp, humidity, wind_speed):
    print(f'Temperature: {temp} Degrees, Humidity: {humidity}%, Wind Speed: {wind_speed}km/h')

display_weather(25, 60, 120)

#Keyword Arguments (Named) Arguments
display_weather(humidity=70, temp=22, wind_speed=15)

#when combining keyword args and positional args in a function call, positional args must come first:
display_weather(70, wind_speed=15, humidity=22)
#display_weather(wind_speed=20, 15, humidity=39)syntax error


#default arguments:
def adjust_lighting(room, brightness=75):
    print(f"Adjusting lighting in {room} to {brightness}% brightness")

adjust_lighting('Living Room')
adjust_lighting('Bedroom', 50)#overriding the brightness value.
















