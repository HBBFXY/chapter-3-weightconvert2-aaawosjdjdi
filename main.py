try:
    weight = float(input())
except:
    exit()
yearly_gain = 0.5
moon_ratio = 0.165
for year in range(0, 11):
    earth_weight = weight + (year * yearly_gain)
    moon_weight = earth_weight * moon_ratio
    print(f"{year}\t{earth_weight:.2f}\t{moon_weight:.2f}")

