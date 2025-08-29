"""
Your module description
"""

# ======================== LIST ===========================
myBooks = ["Atomic Habits", "Filosofi Teras", "Confessions"]
print(myBooks)
print(myBooks[0])
print(myBooks[-2:])
myBooks[1] = "Meditations"
print(myBooks[1])

# ======================== TUPLE ===========================
myTuples = ("Bottle", "Keyboard", "Mouse", "Monitor")
print(myTuples[1])
#myTuples[2] = "Mousepad"
print(myTuples[2])

# ======================== DICTIONARIES ===========================
myPlaylist = [{
    "artist" : "Syudenmagi Online",
    "title" : "escape"
},
{
    "artist" : "Sameko Saba",
    "title" : "The A Team"
}]

print(myPlaylist[1]["artist"])
print(myPlaylist[1]["title"])