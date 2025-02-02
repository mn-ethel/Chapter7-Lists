List=[8,9,10]
List[1]=17
for i in range (4,7):
    List.append(i)
List.remove(List[0])
print(List)
List.sort()
doubled=List*2
doubled.insert(3,25)
print(f"The final result is {doubled}")



