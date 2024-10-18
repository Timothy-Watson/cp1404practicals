"""
CP1404 - Wimbledon
Estimate: 25 min
Actual:
"""

filename = "wimbledon.csv"
with open(filename, "r", encoding="utf-8-sig") as in_file:
    in_file.readline()  # Removes the first line (csv data)
    data = [line.strip().split(',') for line in in_file.readlines()]
player_to_wins = {}
for point in data:
    if point[2] in player_to_wins:  # point[2] is player name
        player_to_wins[point[2]] += 1
    else:
        player_to_wins[point[2]] = 1
print("Wimbledon Champions")
for player in player_to_wins:
    print(f"{player} {player_to_wins[player]}")
