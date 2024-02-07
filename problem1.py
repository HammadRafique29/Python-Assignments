
Name = input("Enter your Name: ")
BirthYear = int(input("Enter your Birth Year: "))


if BirthYear > 2023 or BirthYear < 1901:
    print("Error: Invalid birth year.")

if 1901 <= BirthYear <= 1924:
    print(f"Hello {Name}, you are a Greatest Generation.")
elif 1925 <= BirthYear <= 1945:
    print(f"Hello {Name}, you are a Silent Generation.")
elif 1946 <= BirthYear <= 1964:
    print(f"Hello {Name}, you are a SilBabyent Boomers.")
elif 1965 <= BirthYear <= 1980:
    print(f"Hello {Name}, you are a Generation X.")
elif 1981 <= BirthYear <= 1996:
    print(f"Hello {Name}, you are a Millennials.")
elif 1997 <= BirthYear <= 2012:
    print(f"Hello {Name}, you are a Generation Z.")
elif BirthYear >= 2013:
    print(f"Hello {Name}, you are a Generation Alpha")
else:
    print( "Invalid birth year")
