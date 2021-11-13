# kali=input("enter the number")
# amout=int(input("enter the number"))
# if kali==book:
#     print("no charge")
# elif kali== amout:
#     print("charge")   

n=int(input("Enter number of days: "))
f=1
if n<0:
    print("Invalid Input.")
else:
    if n<=5:
        f=0.4*n
    elif n<=10:
        f=0.65*n
    else:
        f=0.8*n
    print("Fine: ",f)
    # https://youtu.be/ijPpVpMgdI8?t=575