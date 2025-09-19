weight = float(input())
for year in range(11):
    earth = weight + year * 0.5
    moon = earth * 0.165
    print(f"{year}\t{earth:.2f}\t{moon:.2f}")
