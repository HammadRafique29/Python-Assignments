# Output Sequence List
Sequence = [1, 1]
Rational = ["1/1"]

# Considered and Percedent Value
Considered = 1
Percedent = 0


Total = int(input("How Many Numbers To Generate: "))

for i in range(Total):
    # Sum of Considered and Percedent Value
    Result = Sequence[Percedent] + Sequence[Considered]
    # Adding the result in Sequence
    Sequence.append(Result)
    # Lastly we append the Value in Sequence we Considered
    Sequence.append(Sequence[Considered])

    # Increment the Values
    Considered += 1
    Percedent += 1
    
# for i in range(2, len(Sequence), 2):
#     Rational.append(f"{Sequence[i]}/{Sequ10ence[i-1]}")

Rational = []
for i in range(len(Sequence) - 1):
    # Sequence[1] upper Values and Sequencep[i+1] for Lower value
    rational = f"{Sequence[i]}/{Sequence[i + 1]}"
    Rational.append(rational)

print(Sequence[:Total], "\n", Rational[:Total])
