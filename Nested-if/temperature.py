"""
Write a program that classifies the temperature into various categories such as "Freezing", "Cold", "Warm", and "Hot" based on the following conditions:

If the temperature is below 0°C, it is "Freezing".
If the temperature is between 0°C and 10°C, it is "Cold".
If the temperature is between 10°C and 25°C, it is "Warm".
If the temperature is above 25°C, it is "Hot".
"""
t=int(input("temperature:"))
if t>0:
    if t<25:
        if t<10:
            print("cold")
        else:
            print("warm")
    else:
         print("Hot")
else:
    print("Freezing")
