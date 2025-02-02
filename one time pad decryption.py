encrypted = input("\nEnter the encrypted message: ")
shifts = list(map(int, input("Enter the shifts used (comma-separated): ").split(',')))
decrypted = [
        chr(((ord(c) - ord('a') - shift) % 26) + ord('a')) if c.isalpha() else c
        for c, shift in zip(encrypted, shifts)]

print(f"\nDecrypted Message: {decrypted}")

