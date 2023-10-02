"""
x = int(input("Enter the first number: "))
y = int(input("Enter the secound number: "))
print(f"after doing sum {x + y}")
"""

"""
x= "Andrew tate not a misogynist"
print(x[4])
print(x[:3])
print(x[1:2:3]) #:3 -> x-1, hence: :2
"""

#Exercise - 1
print("Welcome to Dictionary!!")
print("Words: 1. Misogynist\n2. Gravely\n3. Walked out")
x= {"Misogynist": "Oppose the girls",
    "Gravely": "Seriously",
    "Walked out": "Get out"
    }
i = input("Enter the word-> ")
print("The correct meaning of this word is " + x[i])