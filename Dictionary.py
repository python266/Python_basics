"""
1. Exersice
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
for i in range(len(keys)):
        x = {keys[i]: values[i]}
        print(x)
"""
"""
#exercise 2
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict["class"]["student"]["marks"]["history"])
"""
"""
#exercise 3
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

x = {employees[0]: defaults}
print(x)
"""

"""
#exercise 4
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

#x = sample_dict[keys[0]], sample_dict[keys[1]]
x = {keys[0]: sample_dict[keys[0]], keys[1]: sample_dict[keys[1]]}
print(x)
"""