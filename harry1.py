print("welcome to Hogwarts")

print("Here is some info on our four houses")

thisdict = {
    "house" : "gryffindor",
    "colors" : "red and gold",
    "alum" : "Ron Weasley"
}
house = input("Which house are you intersted: ")
print(house)
if house == thisdict["house"]:
    print(thisdict["colors"])
 
