# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:53:23 2022

@author: User
"""
"""
15)	Să se afişeze primele n numere care au suma cifrelor mai mică sau egală cu m.
Exemplu: Pentru n=10 şi m=4  se vor afişa numerele 1, 2, 3, 4, 10, 11, 12, 13, 20, 21.


primele  n = 10 ------>> 1, 2, 3, 4, 10, 11, 12, 13, 20, 21.
suma cifrelor mai mică sau egală cu m = 4
"""

n = int(input("Introdu cite cifre doresti sa apara >>> "))
m = int(input("Introdu suma cifrelor >>> "))
tuple_point = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) #int number list which cannot be changed
list_complet = list() #declare new list
k = range(10,250,1) # declare k is list number of 10 to 98.

# first "x" single number from tuple_point
for i in tuple_point: # listing i in tuple_point
  if i < m:
    i = i+1
    list_complet.append(i) #add true result to list complet 
  # lest "xx" two numbers from k= range(10,99)
if n != len(list_complet):
  for j in k:
    # transform number j=10 in string "10" to have acces to [1] and [0]. and compare <> true false
    if int(str(j)[0]) < m and int(str(j)[1]) < m :
      list_complet.append(j) #add true result to list complet
    if n == len(list_complet):      #control if cicle not exceeded the limit n
      print("Lista",list_complet)
      break


      
        
     
         






# sum_m = input("Enter number sum: ")

# firs_ten_num = n

# def firs_num():             
#num_2 [9, 8, 7, 6 ,5, 4, 3, 2 ,1 0]

""" num_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
m = 4
n = 10
  # i = 1  
for i in num_1:
    while i <= m:
      i += 1
      print(i)
      if (i == m):
        break
""   
if m <= len(n):
        for i in num :
            print("Cifra mai mica tablou:", i)"""      
            
"""
str1=str(input("Primele cifre >>>"))
sum2=str(input("Suma cifrelor>>>"))
print(str1)
print(sum2)
k=0
j=0
for elem in str1:
    if elem<=sum2 :
        k=k+1
        print(elem)
print("k=" ,k)
"""