# Dictionary to model the player’s inventory 
# Keys are string values describing the item in the inventory
# Values are integers detailing how many of that item the player has
# Write a function, displayInventory(), that takes an inventory parameter, prints 'Inventory:', then prints value and key for each item, and finishes by printing the total number of items
# I sorted by keys and newlines

# Inventory function
def displayInventory(inventory):
    print('Inventory:\n')
    item_total = 0
    for k, v in sorted(inventory.items()):
        print(str(v) + ' ' + k)
        item_total += v
    print('\nTotal number of items: ' + str(item_total))

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(stuff)
