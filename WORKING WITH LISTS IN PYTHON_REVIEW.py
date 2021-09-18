inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#First, how many items are in the warehouse?
inventory_len = len(inventory)
print(inventory_len)

#Select the first element
first = inventory[1]
print(first)

#Select the last element
last = inventory[-1]
print(last)

#Select items from the inventory starting at index 2 and up to, but not including, index 6
inventory_2_6 = inventory[2:6]
print(inventory_2_6)

#Select the first 3 items
first_3 = inventory[:3]
print(first_3)

#How many 'twin bed's are in
twin_beds = inventory.count("twin bed")
print(twin_beds)

#Remove the 5th element in the inventory
removed_item = inventory.pop(4)
print(removed_item)

#There was a new item added to our inventory called "19th Century Bed Frame".Use the .insert() method to place the new item as the 11th element in our inventory.
inventory.insert(10,"19th Century Bed Frame")

#Sort inventory using the .sort() method or the sorted() function.
inventory.sort()
print(inventory)









