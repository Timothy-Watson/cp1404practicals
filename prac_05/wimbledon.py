"""
CP1404 - Wimbledon
Estimate: 25 min
Actual: 29 min
"""

filename = "wimbledon.csv"
with open(filename, "r", encoding="utf-8-sig") as in_file:
    in_file.readline()  # Removes the first line (csv data)
    data = [line.strip().split(',') for line in in_file.readlines()]
player_to_wins = {}
winning_countries = set()
for point in data:
    if point[2] in player_to_wins:  # point[2] is player name
        player_to_wins[point[2]] += 1
    else:
        player_to_wins[point[2]] = 1
    winning_countries.add(point[3])  # point[3] is country
print("Wimbledon Champions")
for player in player_to_wins:
    print(f"{player} {player_to_wins[player]}")
print()
print(f"These {len(winning_countries)} have won Wimbledon")
print(", ".join(sorted(winning_countries)))
