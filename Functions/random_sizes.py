import random

def random_number(n):
    start = 10**(n-1)
    end = (10 ** n) - 1
    num = random.randint(start, end)
    while (str(num)[0] == '0'):
        num = random.randint(start, end)
    return num


n = int(input("Enter the number of digits: "))
print("Random number =", random_number(n))
