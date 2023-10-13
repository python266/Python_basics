x = ["Add", "Sub", "Multiply", "Divide"]

user_input = input(f"{x}\nEnter your choice: ")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number : "))

if user_input == x[0]:
    print(f"Your answer is {a+b*2}")
elif user_input == x[1]:
    print(f"Your answer is {a-b*2}")
elif user_input == x[2]:
    print(f"Your answer is {a*b*2}")
elif user_input == x[3]:
    print(f"Your answer is {a/b*2}")
else:
    raise Exception("Something went wrong, pls try again")
