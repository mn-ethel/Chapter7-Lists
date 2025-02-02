from random import randint

num_simulations = 10000

# Dictionary to count occurrences of each sum
count_rolls = {i: 0 for i in range(2, 13)}

# Simulate rolling two dice
for _ in range(num_simulations):
    die1 = randint(1, 6)  # Roll first die (1-6)
    die2 = randint(1, 6)  # Roll second die (1-6)
    total = die1 + die2          # Sum of both dice
    count_rolls[total] += 1      # Update count

# Print results
print("Sum | Probability (%)")
print("---------------------")
for total, count in count_rolls.items():
    probability = (count / num_simulations) * 100
    print(f"{total:2}  | {probability:.2f}%")
