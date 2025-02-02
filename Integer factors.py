integer=int(input("Enter integer:"))
factors=[]
for i in range(1,integer+1):
    if (integer%i)==0:
        factors.append(i)
print(f"the factors of {integer} are {factors}")
