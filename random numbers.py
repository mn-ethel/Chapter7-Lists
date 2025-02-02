from random import randint
random_list=[]
for i in range(100):
 random_list =random_list.append(randint(0,1))

max_zeros = 0  #
current_zeros = 0  #

for num in random_list:
    if num == 0:
        current_zeros += 1
        max_zeros = max(max_zeros, current_zeros)
    else:
        current_zeros = 0

# Print the generated list and the longest run of zeros
print("Random list:", random_list)
print("Longest run of zeros:", max_zeros)



