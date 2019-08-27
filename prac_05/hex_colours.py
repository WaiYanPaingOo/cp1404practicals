
COLOR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
               "BlanchedAlmond": "#ffebcd", "blue1": "#0000ff", "BlueViolet": "#8a2be2", "brown": "#a52a2a",
               "burlywood": "#deb887", "CadetBlue": "#5f9ea0"}

color = input("Enter color name: ")
while color != "":

    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    else:
        print("Invalid color name")
    color = input("Enter color name: ")