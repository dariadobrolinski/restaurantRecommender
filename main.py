from data import restaurant_data
import stdio

head = None

class Node:
    def __init__(self, cuisine, name, price, rating, address, nextNode = None):
        self.cuisine = cuisine
        self.name = name
        self.price = price
        self.rating = rating
        self.address = address
        self.nextNode = nextNode

for restaurant in restaurant_data:
    newNode = Node(restaurant[0], restaurant[1], restaurant[2], restaurant[3], restaurant[4])
    if head is None:
        head = newNode
    else:
        current = head
        while current.nextNode:
            current = current.nextNode
        current.nextNode = newNode
        

print("What cuisine would you like to eat today?\n")
targetCuisine = stdio.readString()

def searchCuisine(head, targetCuisine):
    current = head
    matches = []

    while current:
        if current.cuisine == targetCuisine:
            matches.append(current)
        current = current.nextNode

    return matches
    
results = searchCuisine(head, targetCuisine)

if not results:
    print(f"\nNo {targetCuisine} spots found!")
else:
    for node in results:
        print(f"\n{node.name} - Price: {node.price}/5, Rating: {node.rating}/5, - {node.address}\n")

