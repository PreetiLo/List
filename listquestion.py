# def match_words(words):
#       ctr = 0

#   for word in words:
#     if len(word) > 1 and word[0] == word[-1]:
#       ctr += 1
#   return ctr

# print(match_words(['abc', 'xyz', 'aba', '1221']))
# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

# def last(n): return n[-1]

# def sort_list_last(tuples):
#   return sorted(tuples, key=last)

# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

# def sum_list(items):
#     sum_numbers = 0
#     for x in items:
#         sum_numbers += x
#     return sum_numbers
# print(sum_list([1,2,-8]))
# Write a Python program to sum all the items in a list.

# def multiply_list(items):
#     tot = 1
#     for x in items:
#         tot *= x
#     return tot
# print(multiply_list([1,2,-8]))
# Write a Python program to multiplies all the items in a list.

# def max_num_in_list( list ):
#     max = list[ 0 ]
#     for a in list:
#         if a > max:
#             max = a
#     return max
# print(max_num_in_list([1, 2, -8, 0]))



# a = [10,20,30,20,10,50,60,40,80,50,40]

# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)

# print(dup_items)
# Write a Python program to remove duplicates from a list.


# l = []
# if not l:
#   print("List is empty")
# Write a Python program to check a list is empty or not.


# original_list = [10, 22, 44, 23, 4]
# new_list = list(original_list)
# print(original_list)
# print(new_list)
# Write a Python program to clone or copy a list.


# def long_words(n, str):
#     word_len = []
#     txt = str.split(" ")
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len	
# print(long_words(3, "The quick brown fox jumps over the lazy dog"))
# Write a Python program to find the list of words that are longer than n from a given list of words.


# def common_data(list1, list2):
#      result = False
#      for x in list1:
#          for y in list2:
#              if x == y:
#                  result = True
#                  return result
# print(common_data([1,2,3,4,5], [5,6,7,8,9]))
# print(common_data([1,2,3,4,5], [6,7,8,9]))
# Write a Python function that takes two lists and returns True if they have at least one common member.

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# print(color)
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.


# array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
# print(array)
# Write a Python program to generate a 3*4*6 3D array whose each element is *.


# num = [7,8, 120, 25, 44, 20, 27]
# num = [x for x in num if x%2!=0]
# print(num)
# Write a Python program to print the numbers of a specified list after removing even numbers from it.

# from random import shuffle
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# shuffle(color)
# print(color)
# Write a Python program to shuffle and print a specified list.


# def printValues():
#     	l = list()
# 	for i in range(1,21):
# 		l.append(i**2)
# 	print(l[:5])
# 	print(l[-5:])

# printValues()
# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

# import itertools
# print(list(itertools.permutations([1,2,3])))
# Write a Python program to generate all permutations of a list in Python.
# In mathematics, the notion of permutation relates to the act of arranging all the members of a set into some sequence or order, or if the set is already ordered, rearranging (reordering) its elements, a process called permuting. These differ from combinations, which are selections of some members of a set where order is disregarded.
# In the following image each of the six rows is a different permutation of three distinct balls

# list1 = [1, 3, 5, 7, 9]
# list2=[1, 2, 4, 6, 7, 8]
# diff_list1_list2 = list(set(list1) - set(list2))
# diff_list2_list1 = list(set(list2) - set(list1))
# total_diff = diff_list1_list2 + diff_list2_list1
# print(total_diff)
# Write a Python program to get the difference between the two lists.

# nums = [5, 15, 35, 8, 98]
# for num_index, num_val in enumerate(nums):
#     print(num_index, num_val)
# Write a Python program access the index of a list.

# s = ['a', 'b', 'c', 'd']
# str1 = ''.join(s)
# print(str1)
# Write a Python program to convert a list of characters into a string.

# num =[10, 30, 4, -6]
# print(num.index(30))
# Write a Python program to find the index of an item in a specified list.

# import itertools
# original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# new_merged_list = list(itertools.chain(*original_list))
# print(new_merged_list)
# Write a Python program to flatten a shallow list.


# list1 = [1, 2, 3, 0]
# list2 = ['Red', 'Green', 'Black']
# final_list = list1 + list2
# print(final_list)
# Write a Python program to append a list to the second list.

# import random
# color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
# print(random.choice(color_list))
# Write a Python program to select an item randomly from a list.

# list1 = [10, 10, 0, 0, 10]
# list2 = [10, 10, 10, 0, 0]
# list3 = [1, 10, 10, 0, 0]

# print('Compare list1 and list2')
# print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
# print('Compare list1 and list3')
# print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))
# Write a python program to check whether two lists are circularly identical.


# def second_smallest(numbers):
#       if (len(numbers)<2):
#     return
#   if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
#     return
#   dup_items = set()
#   uniq_items = []
#   for x in numbers:
#     if x not in dup_items:
#       uniq_items.append(x)
#       dup_items.add(x)
#   uniq_items.sort()    
#   return  uniq_items[1]   

# print(second_smallest([1, 2, -8, -2, 0, -2]))
# print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
# print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# print(second_smallest([2,2]))
# print(second_smallest([2]))
# Write a Python program to find the second smallest number in a list.

# def second_largest(numbers):
#       if (len(numbers)<2):
#     return
#   if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
#     return
#   dup_items = set()
#   uniq_items = []
#   for x in numbers:
#     if x not in dup_items:
#       uniq_items.append(x)
#       dup_items.add(x)
#   uniq_items.sort()    
#   return  uniq_items[-2]   
# print(second_largest([1,2,3,4,4]))
# print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# print(second_largest([2,2]))
# print(second_largest([1]))
# Write a Python program to find the second largest number in a list.

# my_list = [10, 20, 30, 40, 20, 50, 60, 40]
# print("Original List : ",my_list)
# my_set = set(my_list)
# my_new_list = list(my_set)
# print("List of unique numbers : ",my_new_list)
# Write a Python program to get unique values from a list.

 
# import collections
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# print("Original List : ",my_list)
# ctr = collections.Counter(my_list)
# print("Frequency of the elements in the List : ",ctr)
# Write a Python program to get the frequency of the elements in a list.

# def count_range_in_list(li, min, max):
#     	ctr = 0
# 	for x in li:
# 		if min <= x <= max:
# 			ctr += 1
# 	return ctr

# list1 = [10,20,30,40,40,40,70,80,99]
# print(count_range_in_list(list1, 40, 100))

# list2 = ['a','b','c','d','e','f']
# print(count_range_in_list(list2, 'a', 'e'))
# Write a Python program to count the number of elements in a list within a specified range.

# def is_Sublist(l, s):
#     	sub_set = False
# 	if s == []:
# 		sub_set = True
# 	elif s == l:
# 		sub_set = True
# 	elif len(s) > len(l):
# 		sub_set = False

# 	else:
# 		for i in range(len(l)):
# 			if l[i] == s[0]:
# 				n = 1
# 				while (n < len(s)) and (l[i+n] == s[n]):
# 					n += 1
				
# 				if n == len(s):
# 					sub_set = True
# Write a Python program to check whether a list contains a sublist.



# 	return sub_set

# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))
# Write a Python program to check whether a list contains a sublist.



# from itertools import combinations
# def sub_lists(my_list):
# 	subs = []
# 	for i in range(0, len(my_list)+1):
# 	  temp = [list(x) for x in combinations(my_list, i)]
# 	  if len(temp)>0:
# 	    subs.extend(temp)
# 	return subs


# l1 = [10, 20, 30, 40]
# l2 = ['X', 'Y', 'Z']
# print("Original list:")
# print(l1)
# print("S")
# print(sub_lists(l1))
# print("Sublists of the said list:")
# print(sub_lists(l1))
# print("\nOriginal list:")
# print(l2)
# print("Sublists of the said list:")
# print(sub_lists(l2))
#  Write a Python program to generate all sublists of a list.


# def prime_eratosthenes(n):
#     prime_list = []
#     for i in range(2, n+1):
#         if i not in prime_list:
#             print (i)
#             for j in range(i*i, n+1, i):
#                 prime_list.append(j)

# print(prime_eratosthenes(100));
# Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.


# my_list = ['p', 'q']
# n = 4
# new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
# print(new_list)
# Write a Python program to create a list by concatenating a given list which range goes from 1 to n.


# x = 100
# print(format(id(x), 'x'))
# s = 'w3resource'
# print(format(id(s), 'x')) 
# Write a Python program to get variable unique identification number or string.

# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# print(set(color1) & set(color2))
# Write a Python program to find common items from two lists.

# from itertools import zip_longest, chain, tee
# def replace2copy(lst):
#     lst1, lst2 = tee(iter(lst), 2)
#     return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
# n = [0,1,2,3,4,5]
# print(replace2copy(n))
# Write a Python program to change the position of every n-th value with the (n+1)th in a list.

# L = [11, 33, 50]
# print("Original List: ",L)
# x = int("".join(map(str, L)))
# print("Single Integer: ",x)
# Write a Python program to convert a list of multiple integers into a single integer.

# from itertools import groupby
# from operator import itemgetter

# word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
#      'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

# for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
#     print(letter)
#     for word in words:
#         print(word)
# Write a Python program to split a list based on first character of word.


# obj = {}
# for i in range(1, 21):
#     obj[str(i)] = []
# print(obj)
# Write a Python program to create multiple lists.


# list1 = ['a','b','c','d','e','f']
# list2 = ['d','e','f','g','h']
# print('Missing values in second list: ', ','.join(set(list1).difference(list2)))
# print('Additional values in second list: ', ','.join(set(list2).difference(list1)))
# Write a Python program to find missing and additional values in two lists.

# color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
#          ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
# var1, var2, var3 = color
# print(var1)
# print(var2)
# print(var3)
# Write a Python program to split a list into different variables.

# l = [[5*i + j for j in range(1,6)] for i in range(5)]
# print(l)
# Write a Python program to generate groups of five consecutive numbers in a list.

# L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
#  (7, 8), (9, 10)]
# print("Original List: ", L)
# print("Sorted Unique Data:",sorted(set().union(*L)))
# Write a Python program to convert a pair of values into a sorted unique array.

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(x[::2])
# Write a Python program to select the odd items of a list.

# color = ['Red', 'Green', 'Black']
# print("Original List: ",color)
# color = [v for elt in color for v in ('c', elt)]
# print("Original List: ",color)
# Write a Python program to insert an element before each element of a list.


# colors = [['Red'], ['Green'], ['Black']]
# print('\n'.join([str(lst) for lst in colors]))
# Write a Python program to print a nested lists (each list on a new line) using the print() function.


# color_name = ["Black", "Red", "Maroon", "Yellow"]
# color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])
# Write a Python program to convert list to list of dictionaries.


# my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
# print("Original List: ")
# print(my_list)
# my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
# print("Sorted List: ")
# print(my_list)
# Write a Python program to sort a list of nested dictionaries.










