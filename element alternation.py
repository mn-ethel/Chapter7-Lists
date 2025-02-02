L=list(map(int,input("Enter a list of numbers separated by space:").split()))
new=[L[-1]] + L[:-1]
print(new)
