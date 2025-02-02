first_List=[]
square_list=[]
letter_list=[]
for i in range(50):
    first_List.append(i)
print(f"Integer list:{first_List}")

for i in range(51):
    square_list.append(i*i)
print(f"The squares list:{square_list}")
for i in range (1,27):
    letter_list.append(chr(96+i)*i)
print(f"The letter list:{letter_list}")
