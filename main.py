weight = float(input())
for year in range(11):
    earth_weight = weight + year * 0.5
    moon_weight = earth_weight * 0.165
    print("%d\t%.2f\t%.2f"%(year, earth_weight, moon_weight))

