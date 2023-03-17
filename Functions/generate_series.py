def series(a, b):
    d = int((b - a)/3)
    return[a,a+d, a+2*d, a+3*d]


a = int(input("Enter the first number: "))
b = int(input("Enter the last number: "))
print("The required series is: ", series(a, b))
