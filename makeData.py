import csv
import random
from datetime import datetime, timedelta

# Sample users and locations with coordinates
users = ["jdoe", "asmith", "bwayne", "ckent", "dprince", "pparker", "nsummers"]
locations = [
    ("New York, USA", 40.7128, -74.0060),
    ("London, UK", 51.5074, -0.1278),
    ("Berlin, Germany", 52.52, 13.4050),
    ("Tokyo, Japan", 35.6895, 139.6917),
    ("Sydney, Australia", -33.8688, 151.2093),
    ("San Francisco, USA", 37.7749, -122.4194),
    ("Toronto, Canada", 43.651070, -79.347015),
    ("Paris, France", 48.8566, 2.3522),
    ("Dubai, UAE", 25.276987, 55.296249),
    ("São Paulo, Brazil", -23.55052, -46.633308)
]
devices = ["Laptop", "Mobile", "Tablet", "Desktop"]

# Generate fake logs
num_logs = 100
start_time = datetime(2025, 6, 10, 6, 0, 0)

logs = [["timestamp", "username", "ip_address", "location", "latitude", "longitude", "device"]]

for _ in range(num_logs):
    user = random.choice(users)
    location, lat, lon = random.choice(locations)
    device = random.choice(devices)
    ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
    timestamp = start_time + timedelta(minutes=random.randint(0, 240))
    logs.append([timestamp.isoformat() + "Z", user, ip_address, location, lat, lon, device])

# Save to CSV
filename = "faux_auth_logs.csv"
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(logs)

print(f"Saved to {filename}")

