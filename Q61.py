import dbm
db2 = dbm.open("photo_category","c")
#db2["cat.png"] = "a blue cat"
#db2["flower.png"] = "a yellow rose"
#db2["bread.png"] = "harvest bread"

db2["cat.png"] = "a orange cat"
db2["flower.png"] = "a redrose"
db2["bread.png"] = "sourdough bread"

#print(db2["cat.png"])

for item in db2.keys():
    print(item, db2[item])
