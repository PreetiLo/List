# basic_salary=int(input("enter the salary :"))
# if basic_salary <=10000:
#     hra=20%

# i=50
# while (i>0):
#     print(i)
#     i-=1

# a=int(input("enter any number"))
# for i in range(a,0,-1):
#     for j in range(a,0):
#         print(j)
#     print(i)

# a=[1,2,3,[4,5,6]]
# a1=[]
# i=0
# while i<len(a):
#     if type (a[i]) is not  a1:
#            j=0
#            while j<len(a[i]):
#                a1.append(a[j])
#                j+=1
#     else:
#         i+=1          
# print(a1)

# sum=0
# i=0
# while i<len(a):
#     if type(a[i]) is list:
#         j=0
#         while j<len(a[i]):
#             sum=+a[j]
#             j+=1
#     else:
#         sum=+a[i]
#     i+=1 
# print(sum)  


# a={'a':{'b':10,'c':20},'d':{'e':10}}
# for i,j in a.items():
#     for k in j.keys():
#         print(a[i])


# Basic_Salary = input("Enter Basic Salary :")
# DA = (Basic_Salary * 30) / 100
# HRA = (Basic_Salary * 20) / 100
# Gross_Salary = Basic_Salary + DA + HRA
# if Gross_Salary<=10000:
#     print ("\n\nDearness Allowance 30 % of Basic Salary :" , DA)
# elif Gross_Salary<=20000:    
#     print ("House Rent 20 % of Basic Salary :" , HRA)
# elif Gross_Salary>20000:    
#     print ("Gross Salary :" , Gross_Salary)

def showNumbers(): #28 question number 
    a=int(input("enter the number : "))
    i=0
    while i<a:
        if a%2!=0:
            if i==3:
                print(i,"old")
                break 
        else:
            if i%2==0:     
                print(i,"even")
        i+=1   
showNumbers()

# def Sum_multiples(a,b):
#     sum=0
#     for num in range(a, b + 1):
#         if num % 2!= 0:
# #             # print(num, end = " ")
# #             sum+=num
# #             print(sum)  
# # # Sum_multiples( 4, 19)  
# # Sum_multiples(3,5)        

# # def calculate_sum(a, N): 
# #     m = N / a 
# #     sum = m * (m + 1) / 2
# #     ans = a * sum
  
# #     print("Sum of multiples of ", a, 
# #           " up to ", N, " = ", ans) 
# # calculate_sum(3,5)


# # def sum_of_numbers(limit):
# #     total = 0
# #     for i in range(limit):
# #         if i % 3 == 0 or i % 5 == 0:
# #             total = total + i
# #         i = i + 1
# #         return total
# # userInput = int(input("Enter limiting number: "))
# # plusOne = userInput + 1
# # print(sum_of_numbers(plusOne)) 

# # total_sum = 0
# # for i in range(1000):
# #     if (i%3 == 0 or i%5 == 0):
# #         total_sum = total_sum+i
# # print (total_sum)

# # n = 0
# # for i in range(1,500):
# #      if not i % 5 or not i % 3:
# #          n = n + i
# # print(n)

# # def findSum(n, a, b):
# #     sum = 0
# #     for i in range(0, n, 1):
         
# #         # If i is a multiple of a or b
# #         if (i % a == 0 or i % b == 0):
# #             sum += i
 
# #     return sum
 
# # # Driver code
# # # if __name__ == '__main__':
# # n = 10
# # a = 3
# # b = 5
# # print(findSum(n, a, b))


# from typing import Match


# def sumAP(n, d):
#     n = n//d
 
#     return (n) * (1 + n) * d // 2
 
# # Function to find the sum of all
# # multiples of a and b below n
# def sumMultiples(n, a, b):
 
#     # Since, we need the sum of
#     # multiples less than N
#     n = n-1
#     lcm = (a*b)//Maths.gcd(a, b)
#     return sumAP(n, a) + sumAP(n, b) - \
#                          sumAP(n, lcm)
 
# # Driver code
# n = 10
# a = 3
# b = 5
# print(sumMultiples(n, a, b))