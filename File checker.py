# Write a Python program to read first n lines of a file.
"""
f = open("file1.text")
content = f.readline()

print(content)
f.close()
"""

def file_checker():
    i = input("Enter the file name: ")
    d = str(i)
    with open(d) as f:
        try:
            x = f.readlines()
            print(x)
            f.close()
        except FileNotFoundError:
            raise FileNotFoundError("Sorry! Such type of file doesn't exit! Try again!")
        except Exception:
            raise Exception("Sorry! Something went wrong!")
file_checker()
