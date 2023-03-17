def equal(a, b):
    if a == b:
        return True
    else:
        return False
    

string_1 = input("Enter the first string: ")
string_2 = input("Enter the second string: ")
len_1 = len(string_1)
len_2 = len(string_2)
print("The strings are equal in length: ", equal(len_1, len_2))
