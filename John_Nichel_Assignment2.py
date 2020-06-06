# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:12:35 2020
@author: Nichel Emmanuel John
This program will ask the user for details like their name,
stock symbol for the stock they own (for example for Google that would be GOOGL), 
number of shares they own, purchase price and current price for each stock, 
Based on user's input the program will calcuate the earning or loss to date. 
"""

#User inputs are collected in the below code

name = str(input("Please enter the first name and last name of the stock holder: "))
stock_symbols = ["GOOGL","MSFT","RDS-A","AIG","FB"]
shares_counts = ["125","85","400","235","150"]
purchase_prices = ["772.88","56.60","49.58","54.21","124.31"]
current_prices = ["941.53","73.04","55.74","65.27","172.45"]

#Below code displays the details of stocks to the user   
print ("\nStock Ownership for: " + str(name.title()))
print ("----------------------------------------------------")
print ("STOCK \tSHARE \tEARNING/LOSS")
print ("----------------------------------------------------")
for stock_symbol in stock_symbols:
    if stock_symbol == 'AIG':
       total_earnings = ( (float(current_prices[0]) + float(purchase_prices[0])) * float(shares_counts[0]) )
       print ("\n" + (stock_symbol) + "\t" + (shares_counts[0]) + "\t" + str(total_earnings))
   
#print ("Total " + str(stock_symbol.upper()) +  " shares owned: "  + str(shares_count))
#print ("Purchase Price: " + "$" + str(purchase_price))
#print ("Current Price: " + "$" + str(current_price))
#
##calculating the Earning/loss of investment based on Purchase price, current price and stocks earned
#if purchase_price > current_price:
#        total_earnings = ((purchase_price - current_price) * shares_count)
#        print ("Loss to-date: " + "-$" + str(total_earnings) )
#else:
#        total_earnings = ((current_price - purchase_price) * shares_count)
#        print ("Earnings to-date: " + "$" + str(total_earnings) )
        
print("----------------------------------------------------")
print("End of program")

