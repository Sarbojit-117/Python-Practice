def converter(amt, rate):
    rupee = amt * rate
    return rupee
dollar = int(input("Enter the amount in Dollar: "))
rate = int(input("Enter the Dollar-Rupee index: "))
rupee = converter(dollar, rate)
print("Amount in Rupees:", rupee)