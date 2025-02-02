lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
unique_list = []  # List to store unique elements
for item in lst:
    if item not in unique_list:
        unique_list.append(item)  # Add only if not already in the list
    else:
        unique_list=unique_list
print( unique_list)
