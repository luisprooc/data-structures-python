"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

"""

locations = { 'North America': {'USA': ['Mountain View']} }

# Add elements
locations["North America"]["USA"].append("Atlanta")

locations["Asia"] = {"China": ["Shanghai"]}

locations["Asia"] = {"India": ["Bangalore"]}

locations["Africa"] = {"Egypt": ["Cairo"]}

# Loop cities from North America

for items in locations["North America"].values():
    print(items)

"""