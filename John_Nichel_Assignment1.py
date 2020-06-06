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
stock_symbol = input("Please enter the stock symbol you own: ")
shares_count = int(input("Please enter the number of shares you own for " + stock_symbol.upper() + ": "))
purchase_price = float(input ("Please enter the price for purchasing one share of " + stock_symbol.upper() + ": "))
current_price = float(input ("Please enter the current price for one share of " + stock_symbol.upper() + ": "))

#Below code displays the details of stocks to the user   
print ("\nStock Ownership for: " + str(name.title()))
print ("----------------------------------------------------")
print ("Total " + str(stock_symbol.upper()) +  " shares owned: "  + str(shares_count))
print ("Purchase Price: " + "$" + str(purchase_price))
print ("Current Price: " + "$" + str(current_price))

#calculating the Earning/loss of investment based on Purchase price, current price and stocks earned
if purchase_price > current_price:
        total_earnings = ((purchase_price - current_price) * shares_count)
        print ("Loss to-date: " + "-$" + str(total_earnings) )
else:
        total_earnings = ((current_price - purchase_price) * shares_count)
        print ("Earnings to-date: " + "$" + str(total_earnings) )
        
print("----------------------------------------------------")
print("End of program")

