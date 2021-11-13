# a=[ 'n', 'i', 't', 'i', 'n' ] 
# b=[]
# i=1
# while i<=len(a):
#     b.append(a[-i])
#     i=i+1
# print(b)
# if b==a:
#     print("it is palidrom")
# else:
#     print("it is not palidrom")

# a=["madam"]
# b=[]
# i=0
# while i<len(a):
#     b.append(a[-i])
#     i+=1
# print(b) 
# if b==a:
#     print("its palidrom")
# else:
#     print("ist not palidrom")       



# year=int(input("enter the year "))
# if year%400==0 and year%4==0 and year%100==0:
#     print("its leap year")
# else:
#     print("its not leap year")



# num=int(input("Enter a number:"))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")

# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
# org = "The organization for health, safety, and education"
# a = org.split(" ")

# for i in stopwords:
#     if i in a:
#         a.remove(i)

# final_list = []

# for i in a:
#     if i[-1] !=",":
#         final_list.append(i)
#     else:
#         final_list.append(i[0:-1])

# new = ""
# for i in final_list:
#     new += i[0]

# acro= new.upper()



# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
# sent = "The water earth and air are vital"

# acro = ""
# sent_words = sent.split()
# for word in sent_words:
#     if word not in stopwords:
#         acro = acro + word[:2]
#         if word != sent_words[-1]:
            
#             acro += ". "
# acro = acro.upper()
# print(acro)




# a= ['n','i','t','i','n'] 
# pal = []
# for i in range(len(a)):
#     j = i + 1
#     while j < len(a):
#         sub = a[i:j]
#         if sub == sub[::-1]:
#             pal.append(sub)
#         j += 1
#     i=i+1    


# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")

# a=[1,2,5,6,7]
# i=0
# b=[]
# while i<len(a):
#     b.append(a)
#     i+=1
# print(b)    
