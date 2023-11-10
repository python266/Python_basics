"""
#Ex-1
def fun(a ,b):
    v = a + b
    a = a - b
    print(v, a)
    return v, a

fun(50, 10)
"""
"""
def employee(a, b=9000):
    name = a
    salary = b
    print(f"Name: {name}\nSalary: {salary}")
    return employee
employee("Paul Walker", 12000)
employee("Himesh")
"""

'''
def even_no():
    for i in range(1, 31):
        if i%2==0:
            print(i)
        else:
            pass
    return even_no
even_no()
'''

"""
def largest_no():
    x = [4, 6, 8, 24, 12, 2]
    print(f"The largest number is {max(x)}")

largest_no()  
"""