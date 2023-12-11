def get_windChill_Fahrenheit(temp, speed):
    windChill = 35.74 + 0.6215*temp - 35.75*(speed**0.16) + 0.4275*temp*(speed**0.16)
    return windChill

def convert_toFahrenheit(temp):
    temp = temp * (9/5) + 32
    return temp

speed = 0.00

temp = float(input("What is the temperature? "))
tempType = input("Fahrenheit or Celsius (F/C)? ")

if tempType.upper() == 'C':
    for speed in range(5, 65, 5):
        print(f"At temperature {convert_toFahrenheit(temp)}F, and wind speed {speed} mph, the windchill is: {'%.2f' % get_windChill_Fahrenheit(convert_toFahrenheit(temp), speed)}F")
elif tempType.upper() == 'F':
    for speed in range(5, 65, 5):
        print(f"At temperature {temp}F, and wind speed {speed} mph, the windchill is: {'%.2f' % get_windChill_Fahrenheit(temp, speed)}F")
else:
    print("That's not a valid option!")