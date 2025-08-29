"""
Your module description
"""

myBooks=["Atomic Habits", "Filosofi Teras", "Meditations"]

for book in myBooks:
    print(book)

for index, book in enumerate(myBooks):
    print("{}. {}".format(index+1, book))
    
# Mixed data type
mixedTuple = ("Apple", 1, True, 5.55)
customIndex = 1
for d in mixedTuple:
    print("{}. Nyobain bikin output {}".format(customIndex, str(d)))
    # customIndex = customIndex+1
    customIndex += 1 # alternatif yang lebih keren dari customIndex = customIndex+1