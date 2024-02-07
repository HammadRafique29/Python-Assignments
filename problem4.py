def HCF(x, y):
    # Euclidean Algorithm
    while y!=0:
        x, y = y, x % y
    return x

def LCM(x, y):
    # FIRST Convert UPPER Part Into Positive number - Str than Int
    upper = int(str(x * y))     # |x * y|
    lower = HCF(x, y)           # hcf(x, y)
    lcm = upper // lower
    return lcm



Number1 = int(input("Enter the first integer: "))
Number2 = int(input("Enter the second integer: "))

hcf_result = HCF(Number1, Number2)
lcm_result = LCM(Number1, Number2)

# Display the results
print(f"HCF of {Number1} and {Number2} is: {hcf_result}")
print(f"LCM of {Number1} and {Number2} is: {lcm_result}")
