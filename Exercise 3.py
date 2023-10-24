#Mine Code

x = 20  # accurate number
rounds = 0
while rounds<5: # total rounds
    user_input = int(input("Enter the number to win the game: "))
    rounds = rounds + 1
    if rounds == 5:
        print("\n\tAll rounds are overed")
        break
    if user_input > x:
        print("\nYou're out of the range")
        continue
    elif user_input < x:
        print("\nYou entered less than the real number.")
        continue
    elif user_input == x:
        print("\nCorrect! You won the match")
        break

#Below code made by GPT

x = 20  # The accurate number
rounds = 0
while rounds < 5:  # Total rounds
    user_input = int(input("Enter the number to win the game: "))
    rounds = rounds + 1
    if rounds == 5:
        print("\nAll rounds are over")
        break
    if user_input > x:
        print("\nYou're out of range")
        continue
    elif user_input < x:
        print("\nYou entered less than the real number.")
        continue
    elif user_input == x:
        print("\nCorrect! You won the match")
        break