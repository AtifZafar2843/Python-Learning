# Challenge:
# The program picks a secret number between 1 and 100 (use the random module). The user guesses repeatedly. After each guess, say "Too high" or "Too low". When they get it right, congratulate them, report how many attempts it took, and add a comment on their performance (e.g. 5 or fewer = excellent, 8 or fewer = good, otherwise keep practicing).

# Example:
# I'm thinking of a number between 1 and 100.
# Your guess: 50  -> Too high
# Your guess: 25  -> Too low
# Your guess: 37  -> Correct!
# You got it in 3 attempts. Excellent!

# Solution:
import random

secret_num = random.randint(0, 100)
attemps = 0
guess = None

while guess != secret_num:
    guess = int(input("Guess the number between 0 to 100: "))
    attemps += 1
    if guess > secret_num:
        print("Too high!")
    elif guess < secret_num:
        print("Too low!")
    else:
        print("Congratulation! You're Correct")

if attemps < 7:
    print(f"Excellent! You got the number in {attemps} attemps.")
elif attemps < 10:
    print(f"Good! You got the number in {attemps} attemps.")
else:
    print("Keep practicing!")