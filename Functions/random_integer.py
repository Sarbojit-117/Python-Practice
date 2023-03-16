import random

def get_random_integer(start, end):
    return random.randint(start, end)


start = int(input("Enter the initial number: "))
end = int(input("Enter the final number: "))
for i in range (3):
    print(get_random_integer(start, end))
