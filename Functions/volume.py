def volume(length, breadth, height):
    volume = length * breadth * height
    return volume
l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
h = int(input("Enter the height: "))
print("Volume =", volume(l, b, h))