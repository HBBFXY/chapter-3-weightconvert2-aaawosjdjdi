try:
    weight = float(input("请输入体重:"))
except ValueError
    print("请输入有效数字")
    exit()
yearly_gain = 0.5
moon_ratio = 0.165
print("年份\t地球体重、t月球体重")
for year in range(0, 11):
    earth_weight = weight + (year * yearly_gain)
    moon_weight = earth_weight + moon_ratio
    print(f"{year}\t{earth_weight:.2f}\t\t{moon_weight:.2f}")
