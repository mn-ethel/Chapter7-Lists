L = list(map(int, input("Enter elements of list L separated by spaces: ").split()))
M=list(map(int,input("Enter elements of list M separated by spaces:").split()))
if len(L)!=len(M):
    print("Please enter lists of the same length!")
else:
    for i in range (len(L)):
        N=[L[i]+M[i]]
        print(f"The sum of the lists is {N}")