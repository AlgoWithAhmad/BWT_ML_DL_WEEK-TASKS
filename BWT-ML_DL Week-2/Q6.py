def update_inventory(inventory_dict, item, quantity):
    # Update the inventory by adding or removing the specified quantity
    if item in inventory_dict:
        inventory_dict[item] += quantity
        # Ensure that the quantity does not go below zero
        if inventory_dict[item] < 0:
            inventory_dict[item] = 0
    else:
        # If the item is not in the inventory and quantity is positive, add it
        if quantity > 0:
            inventory_dict[item] = quantity
        else:
            # If trying to remove a non-existing item, set quantity to zero
            inventory_dict[item] = 0

    return inventory_dict

def main():
    # Initialize an inventory dictionary with at least 5 items
    inventory = {
        "apple": 10,
        "banana": 20,
        "orange": 15,
        "mango": 5,
        "grape": 8
    }
    
    # Display initial inventory
    print("Initial Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    
    # Prompt the user to update the inventory by adding or removing quantities of 3 items
    for i in range(3):
        item = input(f"\nEnter the name of item {i+1} to update: ")
        quantity = int(input(f"Enter the quantity to add/remove for {item} (use negative value for removal): "))
        inventory = update_inventory(inventory, item, quantity)
    
    # Display the updated inventory
    print("\nUpdated Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

if __name__ == "__main__":
    main()
