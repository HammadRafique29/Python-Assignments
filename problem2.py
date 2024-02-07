
NUMBER = int(input("Please enter a NUMBER: "))

if NUMBER > 0: 
    num = str(NUMBER)
    # Sum the numbers using List comprehension technique
    result = sum(int(digit) ** len(num) for digit in num)
    if result == NUMBER:
        print(f"{NUMBER} is an Armstrong NUMBER.")
    else:
        print(f"{NUMBER} is not an Armstrong NUMBER.")
else:
    print("Enter non-negative integer.")
    