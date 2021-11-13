# a=int(input("enter the number"))
# if a>0:
#     i=1
#     while i<=10:
#         print(i*2,"positive")
#         i=i+1   
# else:
#     print("negative")
# sum=0
# i=0
# while i<=3:
#     a=int(input("enter the number"))
#     sum=sum+a
#     i+=1
# print(sum)    

# n=int(input("enter the number"))
# i=1
# f=1
# sum=0
# while i<n+1:
#     f*=i
#     i+=1
# print("factorial of",n,"is",f)    

# l=[2,3,4,[5,6,7],8,9,1]
# sum=0
# i=0
# while i<len(l):
#     if type(l[i]) is list:
#         j=0
#         while j<len(l[i]):
#             sum+=l[i][j]
#             j+=1
#     else:
#         sum+=l[i]
#     i+=1
# print(sum)       


# l=[10,2,1,5,3,6,9,8,4,7]
# i=0
# while i<len(l):
#     j=i+1
#     while j<len(l):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
#         j+=1
#     i+=1
# print(l)

# l=[1,3,6,7,10]
# b=[]
# i=1
# while i<11:
#     if i not in l:
#         b.append(i)
#     i+=1
# print(b)        

# output=371,370,153,1643
# n=int(input("enter the number"))
# sum=0
# i=n
# while i>0:
#     d=i%10
#     sum+=d**3
#     i//=10
# if n==sum:
#     print("armstrong number")
# else:
#     print("not a armstrong number")

# i=1
# while i<5:
#     j=0
#     while j<5:
#         print(j,i)
#         j+=1
#     i+=1
