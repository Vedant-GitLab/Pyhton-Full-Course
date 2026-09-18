cities1 = {"Tokyo", "Berlin", "Madrid", "Los Angeles"}
cities2 = {"Berlin", "Tokyo"}
print(cities1.issuperset(cities2))
#superset ka mtlb agar original set me kisi other set ki saari values hai to woh uska subset hoga jaise yahan pr cities1 subset hai qki cities2 ki saari values usme hai citi
cities3 = {"Madrid", "Berlin"}
print(cities3.issubset(cities1))
#cities3, cities1 ka subset hai qki uski saari values pehle se hi cities1 me available hai aur cities1, cities2 ka superset hai