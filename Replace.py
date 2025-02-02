L = list(map(int, input("Enter a list of numbers between 1 and 12: ").split()))

# Replace numbers greater than 10 with 10
L = [10 if i > 10 else i for i in L]

# Print the modified list
print("Modified list:", L)
