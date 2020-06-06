"""
Created on Sat Apr 25 10:41:27 2020

@author: Nichel Emmanuel John
#This program will create a report that calculates the earning or loss
 and percentage of yearly earnings/loss of an investor for stocks.
"""


#Importing function earning_loss(investor_stock_data,company) 
#to calculate earning/loss
from John_Nichel_Assignment_function_4 import earning_loss

#Importing function yearly_percentage(investor_stock_data,company) 
#to calculate percentage of yearly earning/loss
from John_Nichel_Assignment_function_4 import yearly_percentage

#Below are the dictionaries that holds values for stock symbols,
#shares count,ourchase price, current price and purchase date.
investor_stock_data = {  
        'GOOGL': {  
            'number_of_shares': 125,
            'purchase_price': 772.88,
            'current_value': 941.53,
            'purchase_dates':'8/1/2015'
            },
        'MSFT ': { 
            'number_of_shares': 85,
            'purchase_price': 56.60,
            'current_value': 73.04,
            'purchase_dates':'8/1/2015'
            },
        'RDS-A': {
            'number_of_shares': 400,
            'purchase_price': 49.58,
            'current_value': 55.74,
            'purchase_dates':'8/1/2015'
            },
        'AIG  ': {
            'number_of_shares': 235,
            'purchase_price': 54.21,
            'current_value': 65.27,
            'purchase_dates':'8/1/2015'
            },
        'FB   ': {
            'number_of_shares': 150,
            'purchase_price': 124.31,
            'current_value': 172.45,
            'purchase_dates':'8/1/2015'
            },
        'M    ': {
            'number_of_shares': 425,
            'purchase_price': 30.30,
            'current_value': 23.98,
            'purchase_dates':'1/10/2017'
            },
        'F    ': {
            'number_of_shares': 85,
            'purchase_price': 12.58,
            'current_value': 10.95,
            'purchase_dates':'2/17/2017'
            },
        'IBM  ': {
            'number_of_shares': 80,
            'purchase_price': 150.37,
            'current_value': 145.30,
            'purchase_dates':'5/12/2017'
            }     
    }
        
''' Output Report '''
# Stock Ownership Report title with table column headings, 

print('\nStock Ownership for Bob Smith')

print('----------------------------------------------------\n')

print('STOCK              SHARE#                  EARNINGS/LOSS            YEARLY % EARNING/LOSS')
      
print('------------------------------------------------------------------------------------------------------')       
        
# For loop to output the data on each company to the report's detail lines
for company in investor_stock_data:
    
#fetching values for number of shares,stock purchase price,stock current value
    number_of_shares = int(investor_stock_data[company]['number_of_shares']) 
    stock_purchase_price = float(investor_stock_data[company]['purchase_price'])
    stock_current_value = float(investor_stock_data[company]['current_value'])   
    
#Below code displays the report of stocks and the total earnings of the invester.  
    print(company + '               ' + str(number_of_shares) + \
                    '                      ' + '$' + 
          str(earning_loss(investor_stock_data,company)) + \
                    '                    ' +   \
          str(yearly_percentage(investor_stock_data,company )) + '%' )
    
#End of program    
# -======================================================================