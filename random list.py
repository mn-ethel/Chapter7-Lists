from random import randint
L=[]
for i in range (20):
    L.append(randint(1,100))
print(L)
average=sum(L)/len(L)
print(f"The average of the elements in the list is {average}")
L.sort()
largest=L[-1]
smallest=L[0]
print(f"The largest number is {largest}")
print(f"The smallest number is {smallest}")
second_largest=L[-2]
second_smallest=L[1]
print(f"The second largest number is {second_largest}")
print(f"The second smallest number is {second_smallest}")
even_numbers=0
for i in L:
    if i%2==0:
        even_numbers=even_numbers+1
    else:
        even_numbers=even_numbers
print(f"The number of even numbers is {even_numbers}")