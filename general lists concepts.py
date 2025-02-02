L=list(map(int,input("Enter a list:").split()))
length=len(L)
print(f"The total number of items in the list is {length}")
last=L[-1]
print(f"The last item in the list is{last}")
reverse=L[::-1]
print(f"The list in reverse is {reverse}")
if 5 in L:
    print("Yes")
else:
    print("No")
number=L.count(5)
print(f"The number of fives in the list is {number}")
new=(L[1:-1])
new.sort()
print(f"The new sorted list is {new}")
count=0
for i in L:
    if i<5:
        count=count+1
    else:
        count=count
print(f"The number of items less than 5 is {count}")




