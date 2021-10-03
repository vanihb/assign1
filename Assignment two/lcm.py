def cal_lcm(a,b):
    if a>b:
        large=a
    else:
        large=b
    while(True):
        if((large%a == 0) and (large%b == 0)):
            lcm=large
            break
        large += 1
    return lcm
n1=int(input("enter num1:"))
n2=int(input("enter num2:"))
print("lcm of two numbers is:",cal_lcm(n1,n2))
