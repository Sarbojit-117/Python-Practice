def one_place(x):
    a = x % 10
    return a


n = int(input("Enter a positive integer: "))
res = one_place(n)
print("One's digit is =", res)
