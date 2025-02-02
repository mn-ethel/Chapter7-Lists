import random
import string

message = input("Enter a message to encrypt: ")
message = message.lower()
shifts = [random.randint(1, 26) for _ in message]

encrypted_message = [
        chr(((ord(c) - ord('a') + shift) % 26) + ord('a')) if c in string.ascii_lowercase else c
        for c, shift in zip(message, shifts)
]

print(f"\nEncrypted Message: {encrypted_message}")
print(f"Shifts Used: {shifts}")  # Save these shifts for decryption



