print("Welcome to the Coaster")

heights = int(input("Heights in cm "))

if heights >= 120:
    print("Yes")
    age = int(input("What is your age?"))
    if age < 12:
        print("5$")
    elif age <= 18:
        print("7$")
    else:
        print("12")
else:
    print("No")
