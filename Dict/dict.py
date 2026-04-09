empty_dict = {}

# Create a dictionary with some key-value pairs
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}


# Accessing values using keys
print(my_dict["name"])  # Output: Alice shows error if key is not found
print(my_dict.get("age"))  # Output: 30 not shows error if key is not found
print(my_dict.get("country", "Not Found"))  # Output: Not Found

# accesing all keys and values
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # Output: dict_values(['Alice', 30, 'New York'])
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

#modify elements
inventory = {"apples": 5, "bananas": 10, "oranges": 8}
inventory["bananas"] = 12
print(inventory)  # Output: {'apples': 5, 'bananas': 12, 'oranges': 8}

inventory["apples"] = 3
print(inventory)  # Output: {'apples': 3, 'bananas': 12, 'oranges': 8}

#update
new_items = {"grapes": 15, "pears": 7}
inventory.update(new_items)
print(inventory)  # Output: {'apples': 3, 'bananas': 12, 'oranges': 8, 'grapes': 15, 'pears': 7}

#remove elements
del inventory["oranges"]
print(inventory)  # Output: {'apples': 3, 'bananas': 12, 'grapes': 15, 'pears': 7}

popped_value = inventory.pop("bananas")
print(popped_value)  # Output: 12
print(inventory)  # Output: {'apples': 3, 'grapes': 15, 'pears': 7}

#clear
inventory.clear()
print(inventory)  # Output: {}

#membership
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("name" in my_dict)  # Output: True
print("height" in my_dict)  # Output: False

print("Alice" in my_dict.values())  # Output: True
print("30" in my_dict.values())  # Output: False
print(30 in my_dict.values())  # Output: True

#copy
original_dict = {"a": 1, "b": 2, "c": 3}
copied_dict = original_dict.copy()
print(copied_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

#merge

dict1 = {"x": 10, "y": 20}
dict2 = {"y": 30, "z": 40}

dict1.update(dict2)
print(dict1)

dict3={"c": 30, "d": 40}
dict4 = {"d": 10, "e": 20}

merged = dict3 | dict4
print(merged)  # Output: {'c': 30, 'd': 10, 'e': 20}

#len
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(len(my_dict))  # Output: 3

