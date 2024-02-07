Q1 = "Name a country that has played in the rugby world cup final?"
A1 = ["South Africa", "New Zealand", "Australia", "England", "France"]
RESPONSE_COUNT = [26, 22, 23, 29, 0]
# Total guesses
GUESSES = 3

print(min(RESPONSE_COUNT))

print(f"Question: {Q1}")

Result = False
for i in range(GUESSES):
    user_guess = input("Your guess: ")
    for i in range(len(A1)):
        # Loop Through The User Guesses
        if A1[i] == user_guess:
            response = RESPONSE_COUNT[i]
            # Finding The Minimum Response Count
            if min(RESPONSE_COUNT) == response:
                print("Correct! That's a pointless answer.")
                # True Result Verify the Winner and Leave
                Result = True
                break
            else:
                print("Sorry, that's not a pointless answer. Try again.")
    if Result:
        break
                

print("Game over.")