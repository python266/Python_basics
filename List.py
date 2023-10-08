#Exersice for list

"""
#1. Revesed List
x= [100, 200, 300, 400, 500]
y = x[::-1]
print(y)
"""

"""
#2. Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

for i in range(len(list1)):
    print(list1[i] + list2[i])
"""

"""
#3. make square of every number of the list
x= [1,2,3,4,5]
for i in x:
    print(pow(i, 2), end=', ')
"""

"""
#4. Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
for i in range(len(list1)):
    print(list1[i] + list2[i])
"""

"""
#5. Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
x = list1
y= list2[::-1]
for i in range(len(list1)):
    print(str(list1[i]) ," ", str(list2[i]))
"""

"""
EXERCISE 6
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
lsit2 = []
for i in list1:
#    if i.count(i) == 0:
    if i != "":
        lsit2.append(i)
print(lsit2)
"""