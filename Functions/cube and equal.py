import math
def cube(num = 2):
    c = (int(math.pow(num,3)))
    return c
def equal(a, b):
    if a == b:
        return True
    else:
        return False
x = int(input("Enter a number to find its cube: "))
cube = cube(x)
print("Cube =", cube)
a = input("Enter a character: ")
b = input("Enter a character: ")
print("The characters are equal: ", equal(a, b))
