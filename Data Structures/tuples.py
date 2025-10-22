# Create a tuple for your own city (latitude, longitude)
my_city = (7.2906, 80.6337)  # Example: Kandy, Sri Lanka

# Create tuples for 3 friends in different cities
friend1 = (6.9271, 79.8612)   # Colombo, Sri Lanka
friend2 = (13.7563, 100.5018) # Bangkok, Thailand
friend3 = (40.7128, -74.0060) # New York City, USA

# Print the locations of all friends
print("My city:", my_city)
print("Friend 1 (Colombo):", friend1)
print("Friend 2 (Bangkok):", friend2)
print("Friend 3 (New York):", friend3)

# Combine all tuples into one
all_locations = (my_city, friend1, friend2, friend3)
print("\nAll locations combined:", all_locations)

# Optional: Find which friend is the furthest away using approximate distances
from math import radians, sin, cos, sqrt, atan2

def distance(coord1, coord2):
    # Haversine formula to calculate distance (in km)
    R = 6371  # Radius of Earth
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Calculate and print distances
distances = {
    "Friend 1 (Colombo)": distance(my_city, friend1),
    "Friend 2 (Bangkok)": distance(my_city, friend2),
    "Friend 3 (New York)": distance(my_city, friend3)
}

# Display who is furthest
furthest_friend = max(distances, key=distances.get)
print(f"\nThe friend furthest away is {furthest_friend} ({distances[furthest_friend]:.2f} km away).")
