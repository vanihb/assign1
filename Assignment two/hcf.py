def cal_hcf(a, b):

    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1,smaller + 1):
        if((a % i == 0) and (b % i == 0)):
            hcf = i
    return hcf
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("The H.C.F. is", cal_hcf(n1,n2))
