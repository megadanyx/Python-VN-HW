# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 13:18:18 2022

@author: User
"""
usd_eur = 1.47
eur_usd = 0.98
mdl_eur = 20.83
mdl_usd = 18.65

print("#############################")
print("#   Select Input currency:  #")
print("#   * USD                   #")
print("#   * EUR                   #")
print("#   * MDL                   #")
print("#############################")

currency_in = input("choose USD/EUR/MDL >>>")
money_in = float(input("money >>> "))

print("#############################")
print("#   Select output currency: #")
if currency_in != "USD":  # daca varibila nu este egala cu "usd" afirmatia este falsa si cade automat. 
    print("#   * USD                   #")
if currency_in != "EUR":
    print("#   * EUR                   #")
if currency_in != "MDL": 
    print("#   * MDL                   #")
print("#############################")

if currency_in == "USD" : # variabila este egala cu "usd" afirmatia este adevarata si se va afisa rindul respectiv
    currency_out = input("choose EUR/MDL >>>")
elif currency_in == "EUR":
    currency_out = input("choose USD/MDL >>>")
elif currency_in == "MDL":
    currency_out = input("choose USD/EUR >>>")
    
if currency_in == "USD" and currency_out == "EUR" :
   money_out = money_in * usd_eur
   print("Exchange: ", round(money_out, 2))
elif currency_in == "USD" and currency_out == "MDL" :
   money_out = money_in * mdl_usd
   print("Exchange: ", round(money_out, 2))
elif currency_in == "EUR" and currency_out == "USD" :
   money_out = money_in * eur_usd
   print("Exchange: ", round(money_out, 2))
elif currency_in == "EUR" and currency_out == "MDL" :
  money_out = money_in * mdl_eur
  print("Exchange: ", round(money_out, 2))
elif currency_in == "MDL" and currency_out == "USD" :
  money_out = money_in / mdl_usd
  print("Exchange: ", round(money_out, 2))  
elif currency_in == "MDL" and currency_out == "EUR" :
  money_out = money_in / mdl_eur  
  print("Exchange: ", round(money_out, 2))
else:
       print("Ai introdus ceva gresit!")

