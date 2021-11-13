
# a= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]     
# i=0
# lis=[]
# while i<len(a):
#     if a[i] not in lis:
#         lis.append(a[i])
#     i+=1
# print(lis)

# def Repeat(x):
#     _size =len(x)
#     repeated =[]
#     i=0
#     while (i<_size):
#         k=i+1
#         j=0
#         while (j<_size):
#             if x[i] == x[j] and x[i] not in repeated:
#                 repeated.append(x[i])
#             j+=1
#         i+=1
#     return repeated
# a = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]  
# print(Repeat(a))

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
# print (Repeat(a))

# n= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
# i=0
# repeated = []
# while i<len(n):
#     m=n[i]
#     if m not in repeated:
#         repeated.append(m)
#     i=i+1
#     # returnrepeated   
# print(repeated)   

# m= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
# size=len(m)
# repeated=[]
# i=0
# while (i<size):
#     k=i+1
#     j=0
#     while (j< k,size):
#         if k not in repeated:
#             repeated.append(m[i])
#     j=j+1
# print(repeated)    
# b=[]
# i=0
# while i<len(n):
#     count=0
#     j=0
#     while j<len(n):
#         if a[j]==n[i]:
#             count+=1
#         j=j+1
#         if a[i] in b:
#            i+=1
#            continue
#            m.append((n[i])
#            print(n[i],count)
#         i+=1
# print(m)    

# m= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
# n=[]
# o=[]
# i=0
# while i<len(m):
#     m1=0
#     j=0
#     while j<len(m):
#         if m[i]==(m[j]):
#             o.append(m[j])
#             m1=m1+1
#         j=j+1
#     k=0
#     while k<len(m):
#         if m[i] not in n:
#             n.append(m[i])
#             print(m[i]),"times",m1)
#         k=k+1
#     i=i+1


# a= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11,18] 
# b=[]
# c=[]
# i=0
# while i<len(a):
#     c1=0
#     j=0
#     while j<len(a):
#         if a[i]==(a[j]):
#             c.append(a[j])
#             c1=c1+1
#         j=j+1  
#     # i=i+1    
#     k=0
#     while k<len(c):
#         if a[i] not in b:
#             b.append(a[i])
#             print((a[i]),"times",c1)
#         k=k+1
#     i=i+1

# m= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
# n=set(m)
# print (m.count(19))
# print(m.count(17))
# print(m.count(12))



# a = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
# # a = [1,2,9,7,5,1,2,3]
# a.sort()
# item = a[-1]
# for i in range(len(a)-2,-1,-1):
#    if a[i] == item:
#       del a[i]
#    else:
#       item = a[i]
# print (a)

# a=[0, 0, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 2, 2]
# b = []
# prev = None
# for x  in a:
#   if x != prev:
#     b.append(x)
#     prev = x

# print(b)     # [0, 1, 2, 3, 4, 5, 6, 2] 


# i=0
# while(i<10):
#     j = 0
#     while(j<=5):
#         print(j)
#         j = j + 1
#     i = i + 1

