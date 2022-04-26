# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 12:06:48 2022

@author: User
"""
# HW add bill 20. (1, 5, 20)

money = int( input("Enter $: "))


bills_20       = money // 20 * (money >= 20)
bills_rest_20  = money %  20
bills_5        = bills_rest_20 // 5 * (bills_rest_20 >= 5)
bills_1        = money  %  5


print( bills_20,"x $20|" ,bills_5,"x $5|", bills_1,"x $1")