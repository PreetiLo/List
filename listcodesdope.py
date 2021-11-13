# i=10
# a=[]
# while i>0:
#     print("enter number")
#     num=input()
#     a.append(num)
#     i=i-1
# print(a) 
# Take 10 integer inputs from user and store them in a list and print them on screen.


# i=10
# a=[]
# while i>0:
#     print("enter number")
#     num=input()
#     a.append(num)
#     i=i-1
# print("enter a number")
# n=input()
# i=9
# count=0
# while i>=0:
#     if n==a[i]:
#         print("yes")
#         count=count+1
#     i=i-1
# if count ==0:
#     print("no")
#     if n in a:
#         print("yes")
# else:
#     print("no 1")                    
# Take 10 integer inputs from user and store them in a list. Again ask user to give a number. Now, tell user whether that number is present in list or not.
# ( Iterate over list using while loop ).


# i=20
# a=[]
# while i>0:
#     print("enter number")
#     num=input()
#     a.append(num)
#     i=i-1
# old=0
# even=0
# positive=0
# ne    


# Duplicate

# a= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 

#    print(a[1,3,4,7,11,14])
#    print(a[2,9,12])
#    print(a[0,10])


# def Repeat(x): 
#     _size = len(x) 
#     repeated = [] 
#     for i in range(_size): 
#         k = i + 1
#         for j in range(k, _size): 
#             if x[i] == x[j] and x[i] not in repeated: 
#                 repeated.append(x[i]) 
#     return repeated 
  
# # Driver Code 
# a= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
# # print (Repeat(a))
# def Repeat(x):
#     size=len(x)
#     repeat =[]
#     i=0
#     while (i <size):
#         k=i+1
#         j=0
#         while (k,size):
#             if x[i] == x[j] and x[i] not in repeated:
#                 repeated.append(x[i])
#     return repeated 
# a= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]     
# print(Repeat(a)) 


# from math import sqrt
# def primes(n):
#     if n == 0:
#         return []
#     elif n == 1:
#         return []
#     else:
#         p = primes(int(sqrt(n)))
#         no_p = {j for i in p for j in range(i*2, n+1, i)}
#         p = {x for x in range(2, n + 1) if x not in no_p}
#     return p

# for i in range(1,50):
#     print(i, primes(i))
