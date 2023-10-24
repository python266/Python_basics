#for loop exercise
x= ["Himesh", "Listen!", 123, 5]
for item in x:
    if isinstance(item,int):
        c = item
        if c>6:
            print(c)
    else:
        pass