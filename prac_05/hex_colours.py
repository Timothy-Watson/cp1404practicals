"""CP1404/CP5632 Practical - Colour names to hex"""

COLOUR_TO_HEX = {"Absolute Zero": "#0048ba", "Candy Apple Red": "#ff0800", "Green Lizard": "#a7f432",
                 "Honolulu Blue": "#006db0", "MediumOrchid": "#ba55d3", "School Bus Yellow": "#ffd800",
                 "Zomp": "#39a78e", "Tropical Rainforest": "#00755e", "Smoky Black": "#100c08", "GhostWhite": "#f8f8ff"}

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()
print("Farewell")
