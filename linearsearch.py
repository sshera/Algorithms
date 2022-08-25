def index_of_items(collection, target):
    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    return None


names = [
    "Alice",
    "Bob",
    "Calvin",
    "Desiree",
    "Esther",
    "Felix",
    "Gilbert",
    "Helena",
    "Iris",
    "James",
    "Kevin",
    "Linda",
    "Marjorie",
]

search_names = ["Desiree", "Calvin", "Kevin", "Helena"]

for n in search_names:
    index = index_of_items(names, n)
    print(index)
