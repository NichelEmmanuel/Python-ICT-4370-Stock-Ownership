# -*- coding: utf-8 -*-
#"""
#Created on Sat Apr  18 20:12:35 2020
#@author: Nichel Emmanuel John
#This program will create a report that calculates the earning or loss of an investor for stocks.
#"""

#Below are the dictionaries that holds values for stock symbols,shares count,ourchase price and current price.

stock_ownership = {'Bob Smith' : 
    { 
     'stock_symbols' : ['GOOGL', 'MSFT', 'RDS-A', 'AIG', 'FB'],
     'shares_counts' : [125,85,400,235,150],
     'purchase_prices' : [772.88,56.60,49.58,54.21,124.31],
     'current_prices' : [941.53,73.04,55.74,65.27,172.45]
     }
    }

#Below code displays the name of the invester   
for user, values in stock_ownership.items():
    print("\nStock ownership for "+ user)
    print ("-----------------------------------------")
    print("\nSTOCK     SHARE#     EARNING/LOSS")
    print("-----------------------------------------")
    
#Below code displays the report of stocks and the total earnings of the invester.  
for i in range(len(values['stock_symbols'])):
    print("\n"+ values ['stock_symbols'][i]  +  "     "  +  str(values ['purchase_prices'][i] ) + "       " + 
          str (round (values ['current_prices'][i] - values['purchase_prices'][i],2) * round (values ['shares_counts'][i], 2) ) )
    
#End of Program

