initial_weight = float(input())
for year in range(1,11):
    earth_weight = intiatl_weight + year * 0.5
    moon_weight = earth_weight * 0.165
    print(f"{year}{earth_weight:.1f}{moon_weight:.3f}")
