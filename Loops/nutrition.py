fruits = {
    "apple": 130,
    "banana": 110,
    "avocado": 50,
    "sweet cherries": 100,
    "pear": 100,
    "kiwifruit": 90
}

name = input("Fruit: ").lower()

if name in fruits:
    print(fruits[name])
