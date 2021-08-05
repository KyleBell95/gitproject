def printRequest(request):
    for x in (request):
        input ("Give me a " + x)
    return request



#main
request = [ "adjective:", "animal:", "vehicle:", "verb:", "color:", "noun:", "food1:", "food2:", "person:", "saying:"]
printRequest(request)



print("Today I went to my favorite Taco Stand called the " + adjective + " " + animal + ". Unlike most food stands, they cook and prepare the food in a " + somethingRiddenIn + " while you " + verb + ". The best thing on the menu is the " + color + " " + noun + ". Instead of ground beef they fill the taco with " + food1 + ", cheese, and top it off with a salsa made from " + food2 + ". If that doesn't make your mouth water, then it's just like " + person + " always says " + saying + "!" )

#Today I went to my favorite Taco Stand called the
#  {adjective} {animal}. Unlike most food stands, they cook and prepare 
# the food in a {something ridden in} while you {verb}. 
# The best thing on the menu is the {color} {noun}. 
# Instead of ground beef they fill the taco with {foods}, cheese, and top it off
#  with a salsa made from {foods}. If that doesn't make your mouth water, then it' just 
# like {person} always says: {saying}!
