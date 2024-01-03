# reversed a list
num = [1, 2, 3, 4, 5]
reversed_list = num[::-1]
print("Reversed list:", reversed_list)

# another way
num = [1, 2, 3, 4, 5]
num.reverse()
print("Reversed list:", num)

# length of list
lisst = [1, 2, 3, 4, 5]
length_of_list = len(lisst)

print("Length of the list:", length_of_list)

# arrange the list into ascending order
num = [4, 2, 7, 1, 9]
sorted_list = sorted(num)

print("Original list:", num)
print("Sorted list in ascending order:", sorted_list)

# remove duplicate elements form list
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(original_list))

print("Original list:", original_list)
print("List without duplicates:", unique_list)

#convert list into dictionay
keys = ['a', 'b', 'c']
values = [1, 2, 3]

my_dict = dict(zip(keys, values))

print("List of keys:", keys)
print("List of values:", values)
print("Dictionary:", my_dict)

