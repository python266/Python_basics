"""
#how to use while loop
i = 0
while (i<=15):
    print(i)
    i = i+1
"""

while True:
    user_input = int(input("Enter the a number: "))
    if user_input < 100:
        continue
    elif user_input > 100:
         print("You've congratulation. You've entered more than 100")
    break