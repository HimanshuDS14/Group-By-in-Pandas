import pandas as pd


data  = pd.read_csv("weather_by_cities.csv")
print(data.head(10))


g = data.groupby("city")
print(g)
print("\n\n")

for city , data in g:
    print(city)
    print(data)
    print("\n")


print(g.get_group("mumbai"))
print(g.max())
print(g.mean())
print(g.describe())


