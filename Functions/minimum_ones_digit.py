def minimum_digit(a, b):
    a_one = a % 10
    b_one = b % 10
    if a_one < b_one:
        return a
    else:
        return b


inp_1 = int(input("Enter the first number: "))
inp_2 = int(input("Enter the second number: "))
print ("The number with the minimum one's digit =", minimum_digit(inp_1, inp_2))
