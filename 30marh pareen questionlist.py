# i=0
# while i<=5:
#     j=1
#     while j<=6-i:
#         print(" ",end=" ")
#         j+=1
#     h=1
#     while h<=i:
#         print("*",end=" ")
#         h+=1
#     print()
#     i+=1

# a=[]
# b=input("enter any thing ")
# lenght=len(a)
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         lenght.append(a)
#     j+=1
#     d=input("enter ") 
#     if d=="Done":
#         print("")
#         lenght.remove(a)
#     print()
#     i+=1

# a=[]
# i=1
# num=int(input("enter a number"))
# while i<=num:
#     list_d=input("enter number")
#     a.append(list_d)
#     i=i+1
# print(a)
# b=[]
# j=0
# while j<len(a):
#     if a[j] not  in b:
#         b.append(a[j])
#     j=j+1
# print("Done")
# print(b)


# input_string = input("Enter family members separated by comma ")
# family_list  = input_string.split(",")
# print("Printing all family member names")
# for name in family_list:
#     print(name)


# input_string = input("Enter a list element separated by space ")
# list  = input_string.split()
# print("Calculating sum of element of input list")
# sum = 0
# for num in list:
#     sum += int (num)
# print("Sum = ",sum)

# # creating an empty list
# lst = []
# # number of elemetns as input
# n = int(input("Enter number of elements : "))
# # iterating till the range
# for i in range(0, n):
#             ele = int(input())
#             lst.append(ele) # adding the element
# print(lst)

# try:
#     my_list = []    
#     while True: 
#         my_list.append(int(input()))        
# # if input is not-integer, just print the list 
# except: 
#     print(my_list)

# lst = [ ]
# n = int(input("Enter number of elements : "))
# for i in range(0, n):
#     ele = [input(), int(input())]
#     lst.append(ele)
# print(lst)
# print("done")



# # Creating a List with
# # the use of Numbers
# # (Having duplicate values)
# List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
# print("\nList with the use of Numbers: ")
# print(List)

# # Creating a List with
# # mixed type of values
# # (Having numbers and strings)
# List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
# print("\nList with the use of Mixed Values: ")
# print(List)


# Python program to demonstrate
# Addition of elements in a List

# # Creating a List
# List = []
# print("Initial blank List: ")
# print(List)

# # Addition of Elements
# # in the List
# List.append(1)
# List.append(2)
# List.append(4)
# print("\nList after Addition of Three elements: ")
# print(List)

# # Adding elements to the List
# # using Iterator
# for i in range(1, 4):
# 	List.append(i)
# print("\nList after Addition of elements from 1-3: ")
# print(List)

# # Adding Tuples to the List
# List.append((5, 6))
# print("\nList after Addition of a Tuple: ")
# print(List)

# # Addition of List to a List
# List2 = ['For', 'Geeks']
# List.append(List2)
# print("\nList after Addition of a List: ")
# print(List)




# Python program to demonstrate
# Removal of elements in a List

# Creating a List
# List = [1, 2, 3, 4, 5, 6,
# 		7, 8, 9, 10, 11, 12]
# print("Intial List: ")
# print(List)

# # Removing elements from List
# # using Remove() method
# List.remove(5)
# List.remove(6)
# print("\nList after Removal of two elements: ")
# print(List)

# # Removing elements from List
# # using iterator method
# for i in range(1, 5):
# 	List.remove(i)
# print("\nList after Removing a range of elements: ")
# print(List)