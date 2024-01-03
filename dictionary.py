#merging two  dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {**dict1, **dict2}

print("Merged dictionary:", merged_dict)

#for checking key-value pair
my_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_check = 'b'
value_to_check = 2

if my_dict.get(key_to_check) == value_to_check:
    print(f"The key-value pair '{key_to_check}': {value_to_check} exists in the dictionary.")
else:
    print(f"The key-value pair '{key_to_check}': {value_to_check} does not exist in the dictionary.")

# for changing key-value pairs into new one
my_dict = {'old_key': 'value'}

old_key_name = 'old_key'
new_key_name = 'new_key'
new_dict = {new_key_name: my_dict[old_key_name]}

print("Original dictionary:", my_dict)
print("Updated dictionary:", new_dict)

# for inserting key-value pairs
my_dict = {'a': 1, 'b': 2}

   # Insert a new key-value pair using update()
my_dict.update({'c': 3})

print("Updated dictionary:", my_dict)

# sum of keyvalue pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}
sum_of_values = sum(my_dict.values())

print("Sum of values:", sum_of_values)
