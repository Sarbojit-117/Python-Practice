import math
def nthroot(x, n = 2):
    root = math.pow(x, 1/n)
    return root


inp = float(input("Enter a number: "))
n_value = int(input("Enter the value of n: "))
nth_root = nthroot(n_value, inp)
print("The nth root is =", nth_root)
