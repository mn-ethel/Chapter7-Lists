S=input("Enter a list of strings:").split()
new_S=[s[1:] for s in S if len(s)>0]
print(f"The modified strings are:{new_S}")