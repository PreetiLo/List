# C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# def list_slice(S, step):
#     return [S[i::step] for i in range(step)]
# print(list_slice(C,3))
# Write a Python program to split a list every Nth element.

# from collections import Counter
# color1 = ["red", "orange", "green", "blue", "white"]
# color2 = ["black", "yellow", "green", "blue"]
# counter1 = Counter(color1)
# counter2 = Counter(color2)
# print("Color1-Color2: ",list(counter1 - counter2))
# print("Color2-Color1: ",list(counter2 - counter1))
# Write a Python program to compute the difference between two lists.


# import itertools
# c = itertools.count()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# Write a Python program to create a list with infinite elements.


# color = ['red', 'green', 'orange']
# print('-'.join(color))
# print(''.join(color))
# Write a Python program to concatenate elements of a list.


# original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]
# print("Original List: ")
# print(original_list)
# new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in original_list]
# print("New List: ")
# print(new_list)
# Write a Python program to remove key values pairs from a list of dictionaries.


# import ast
# color ="['Red', 'Green', 'White']"
# print(ast.literal_eval(color))
# Write a Python program to convert a string to a list.


# color1 = ["green", "orange", "black", "white"]
# color2 = ["green", "green", "green", "green"]

# print(all(c == 'blue' for c in color1))
# print(all(c == 'green' for c in color2))
# Write a Python program to check whether all items of a list is equal to a given string.


# num1 = [1, 3, 5, 7, 9, 10]
# num2 = [2, 4, 6, 8]
# num1[-1:] = num2
# print(num1)
# Write a Python program to replace the last element in a list with another list.


# x = [1, 2, 3, 4, 5, 6]
# xlen = len(x)-1
# print(x[xlen])
# Write a Python program to check whether the n-th element exists in a given list.


# x = [(4, 1), (1, 2), (6, 0)]
# print(min(x, key=lambda n: (n[1], -n[0])))
# Write a Python program to find a tuple, the smallest second index value from a list of tuples.



# n = 5
# l = [{} for _ in range(n)]
# print(l)
# Write a Python program to create a list of empty dictionaries.
#  quetion number 61 tak kiya hai or krna hai.










# using System;  
# using System.Collections.Generic;  
# using System.Linq;  
# using System.Text;  

# class  LinqExercise18
#     {  
#         static void Main(string[] args)  
#       {  
           
#             List<string> listOfString = new List<string>();  
#             listOfString.Add("m");  
#             listOfString.Add("n");  
#             listOfString.Add("o");  
#             listOfString.Add("p");  
#             listOfString.Add("q");  
			
			
#             Console.Write("\nLINQ : Remove Items from List by creating object internally by filtering  : "); 
#             Console.Write("\n--------------------------------------------------------------------------\n");
            
#             var _result1 = from y in listOfString  
#             select y; 
#             Console.Write("Here is the list of items : \n");
#             foreach(var tchar in _result1)  
#             {  
#                 Console.WriteLine("Char: {0} ", tchar);  
#             } 
 
#             listOfString.Remove(listOfString.FirstOrDefault(en => en == "p")); 
           
 
#             var _result = from z in listOfString  
#             select z;  
#   	    Console.Write("\nHere is the list after removing the item 'p' from the list : \n");
#             foreach(var rChar in _result)  
#             {  
#                 Console.WriteLine("Char: {0} ", rChar);  
#             }  
  
#             Console.ReadLine();  
#         }  
#     }
# Write a program in C# Sharp to Remove Items from List by creating an object internally by filtering.



	