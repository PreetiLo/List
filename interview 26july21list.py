# a=[1,-1,2,-4,7,8,-4]
# output [1,0,2,0,7,8,0]
# a=[1,-1,2,-4,7,8,-4]
# i=0
# b=[]
# while i <len(a):
#     if a[i] < 0:
#         print (a[-i]+1)  
#     else:
#         print(a[i])
#         b.append (a[i]) 
#     i=i+1
# print(b)


# import random

# number_list = [19, 11, 21, 28, 35, 42, 49, 56, 63, 70]
# print("Original list:", number_list)

# random.shuffle(number_list)
# print("List after first shuffle:", number_list)

# random.shuffle(number_list)
# print("List after second shuffle:", number_list)
# import random
# Room_shuffling=[

#         ["room no one","room no two","room no three","room no four","room no five"],
#         ["bed no one","bed no two","bed no three","bed no four","bed no five"],
#         ["Aabiru","jabeena","karona","chaya","deepu","Roshni"]

# ]
# number_of_bed = [19, 11, 21, 28, 35, 42, 49, 56, 63, 70]
# print("Original list:", number_of_bed)
# print("Original list:",Room_shuffling)
# def shuffle_in_place(container):
#        for index in range(len(container) - 1, 0, -1):
#            for i in range (Room_shuffling,number_of_bed):
#             other = random.randint(0, index)
#             other = random.randint(0,Room_shuffling,number_of_bed)
#             if other == index:
#                continue
#             container[index], container[other] = container[other], container[index]

# if __name__ == '__main__':
#     main()
# else:
#     print
