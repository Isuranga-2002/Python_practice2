# 🏈 Kansas City Chiefs Player Dataset

players = [
    {
        'name': 'Patrick Mahomes',
        'position': 'Quarterback',
        'jersey': 15,
        'yards_gained': 4100,
        'touchdowns': 38
    },
    {
        'name': 'Travis Kelce',
        'position': 'Tight End',
        'jersey': 87,
        'yards_gained': 1250,
        'touchdowns': 12
    },
    {
        'name': 'Isiah Pacheco',
        'position': 'Running Back',
        'jersey': 10,
        'yards_gained': 980,
        'touchdowns': 9
    },
    {
        'name': 'Rashee Rice',
        'position': 'Wide Receiver',
        'jersey': 4,
        'yards_gained': 1100,
        'touchdowns': 10
    }
]

# 🏟 Print all player positions
positions = [player['position'] for player in players]
print("Player Positions:", positions)
print("------------------------------------------------")

# 🔁 Update a player's stats (e.g., add yards to Mahomes)
for player in players:
    if player['name'] == 'Patrick Mahomes':
        player['yards_gained'] += 250
        player['touchdowns'] += 2

# ✅ Confirm update
print("Updated Mahomes stats:", [p for p in players if p['name'] == 'Patrick Mahomes'][0])
print("------------------------------------------------")

# 📊 Calculate average yards and touchdowns for all players
total_yards = sum(player['yards_gained'] for player in players)
total_touchdowns = sum(player['touchdowns'] for player in players)
num_players = len(players)

avg_yards = total_yards / num_players
avg_touchdowns = total_touchdowns / num_players

print(f"Average Yards Gained per Player: {avg_yards:.2f}")
print(f"Average Touchdowns per Player: {avg_touchdowns:.2f}")
print("------------------------------------------------")

# 🏆 Summary Output
print("Team Performance Summary:")
for player in players:
    print(f"{player['name']} ({player['position']}) - {player['yards_gained']} yards, {player['touchdowns']} TDs")
