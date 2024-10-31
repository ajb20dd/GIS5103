This is a demo package to calculate the arc distance between two locations. It requires the lat/long coords for both locations.

# Installation

```bash
pip install packagedemo
```

# Example

```bash
# Creating two POIs
poi1 = Location("State Capitol", 30.4383, -84.2807)

poi2 = Location("Union", 30.4445, -84.2970)

# Calculating distance between them
distance = poi1.calculate_distance(poi2)

print(f"Distance between {poi1.name} and {poi2.name}: {distance:.2f} km")
```