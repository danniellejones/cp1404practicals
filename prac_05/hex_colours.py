"""
CP1404 | Prac_05 | Dannielle Jones
Program that looks up colour and finds the hex colour code.
"""

HEX_COLOURS = {"alice blue": "#f0f8ff", "antiquewhite": "#faebd7", "beige": "#f5f5dc", "black": "#000000",
               "blanchedalmond": "#ffebcd", "blueviolet": "#8a2be2", "brown": "#a52a2a", "burlywood": "#deb887",
               "cadetblue": "#5f9ea0", "chocolate": "#d2691e"}

colour = input("Colour: ").lower()
while colour != "":
    if colour in HEX_COLOURS:
        print("{} is {}".format(colour, HEX_COLOURS[colour]))
    else:
        print("Not in colours")
    colour = input("Colour: ").lower()
