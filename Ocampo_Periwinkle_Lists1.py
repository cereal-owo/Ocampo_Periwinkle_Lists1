items = ["Burger", "Nuggets", "Fries", "Chicken", "Soda"]
print (f"Original items: {items}")
index_upd = int(input("Choose an index number to update/replace: "))
new_value = input("Input a new value: ")
items[index_upd] = new_value
slice1 = int(input("Enter slice range 1: "))
slice2 = int(input("Enter slice range 2: "))
search_item = input("Search an item: ")
print(f"Updated list: {items}")
print(f"Sliced list: {items[slice1:slice2]}")
if search_item in items:
    print(f"{search_item} is in list")
else:
    print("Item is not in list")