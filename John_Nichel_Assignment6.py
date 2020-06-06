"""
Created on Sunday May 11 22:44:23 2020
@author: Nichel Emmanuel
# Python Version: 3.7.7.
# Week 6 Programming Assignment: Files and 

Description: Below Code will read and write text files in Python.   
Unlike Assignment 5, instead of hard coding the data, 
The data is populated using two text files which holds data for stock and other for bond.
Stock file(Lesson6_Data - Stocks.txt) and the one bond (Lesson6_Data - Bond.txt)
Instead of printing the report to the screen, output is printed to a separate text file.
Three classes are created for investor, Stock data and bond which is inherited from Stock class.
And the required number of methods are defined to calculate gain/loss, yeatly earnings
and yield percentage in the respective classes.
"""

# Set up the stock data variables as class attributes and functions as stock class methods.class stock_ownership():
class Stock():
    #fetching values for stock symbols,number of shares,purchase price, 
    #current price of the stock and purchase date.
    def __init__(self,purchase_ID,stock_symbol,number_of_shares,stock_purchase_price,stock_current_value,stock_purchase_date):

        '''Initialize the stock attributes '''

        self.stock_symbol = stock_symbol
        self.number_of_shares = number_of_shares
        self.stock_purchase_price = stock_purchase_price
        self.stock_current_value = stock_current_value
        self.stock_purchase_date = stock_purchase_date
        self.purchase_ID = purchase_ID
    
    #fucntion to calculate the earning or loss of stock.     
    def calculate_earnings_loss(self):

        #formula = (current value – purchase price) x number of shares
        calculate_earnings_loss = self.number_of_shares * (self.stock_current_value - self.stock_purchase_price)

        return ("$" + format(calculate_earnings_loss, ',.2f'))
        
    #function to calculate the yearly earnings/loss.      
    def calculate_earnings_percentage(self):  

        return (self.stock_current_value - self.stock_purchase_price) / self.stock_purchase_price
    
    #function to calculate the percentage of yearly earnings/loss.             
    def calculate_yearly_rate_earnings(self):

      
        from datetime import datetime        
         #formula used = ((((current value – purchase price)/purchase price)/
        #              (current date – purchase date)))*100       
        days_interval = datetime.now() - datetime.strptime(self.stock_purchase_date,"%m/%d/%Y")  

        return (self.calculate_earnings_percentage()/(days_interval.days/365))*100
       

#Below class is written to create a Bond. it holds value for Bond coupon and Bond yield
class Bond(Stock):

    def __init__(self,stock_symbol,number_of_shares,stock_purchase_price,stock_current_value, stock_purchase_date):
    
        super().__init__(stock_symbol,number_of_shares,stock_purchase_price,stock_current_value, stock_purchase_date)

        self.bond_coupon = 0.0  

        self.bond_yield = 0.0
       
       
#Creating the investor class
class Investor:

    def __init__(self,name,address, phone):

       #setup values for the investor clas name, address,and phone number

        self.name=name
        self.address = address
        self.phone = phone
       
#Input section          
#Below code holds values for stock symbols,
#shares count,purchase price, current price and purchase date.

company_stocks = []
stock_file_name = 'Lesson6_Data - Stocks.txt'

try:
 stock_purchase_ID = 1
 raw_stock_data = []
 stock_line_counter = 5

 with open(stock_file_name) as stock_file_object:
 #line = file_object.readlines()
   stock_lines = stock_file_object.readlines()

except FileNotFoundError:
 print('File not found ' + stock_file_name + ' file.\n')
 
while stock_line_counter < len(stock_lines):

#while(raw_stock_data_ID < len(raw_stock_data)):
 try:
  company_stocks.append(Stock(stock_line_counter,
  stock_lines[stock_line_counter].rstrip(),
  int(stock_lines[stock_line_counter + 1].rstrip()),
  float(stock_lines[stock_line_counter + 2].rstrip()),
  float(stock_lines[stock_line_counter + 3].rstrip()),
  stock_lines[stock_line_counter + 4].rstrip()))
 
  stock_purchase_ID += 1
 
 except ValueError:
     print('values could not be converted to a int or float. \n')
     stock_line_counter += 5
     
                   
   
#input data for Bond investment stock symbols,number of shares,purchase price, 
#current price of the stock and purchase date.
bonds_filename = 'Lesson6_Data - Bond.txt'
#company_bonds_owned = build_company_bonds_owned(bonds_filename)

# Output will be printed in below file
output_file_name = 'John.Nichel.Assignment-report-6.txt'
''' Output Report '''
# Stock Ownership Report title with table column headings
#Below section print report for stocks owned
with open(output_file_name, 'w') as file_object:
    file_object.write('Stock ownership for Bob Smith\n')
    file_object.write('----------------------------\n')
    file_object.write('\nSTOCK        SHARE#          EARNINGS/LOSS \n')
    file_object.write('---------------------------------------------\n')
    
 #Below code displays the report of stocks and the total earnings of the investor. 
for stock in company_stocks:
 file_object.write(stock.company_stock_data
                   + '          ' + str(stock.number_of_shares) 
                   + '          ' + stock.loss_or_gain() + '\n')

#Below section print report for bond owned and its data.
 file_object.write('\n---------------------------------------------\n')
 file_object.write('Bond ownership for Bob Smith\n')
 file_object.write('----------------------------\n')
 file_object.write('---------------------------------------------\n')

#Below code displays the report of bonds and the total earnings of the investor. 
company_bonds = {}
for bond in company_bonds:
 file_object.write(bond.company_stock_data 
                   + '          ' + str(bond.number_of_shares)
                   + '          ' + bond.loss_or_gain() + '\n')

import calendar
import locale
from datetime import datetime, date

def get_yield_percentage(current_price, purchase_price, purchase_date):
 DAY_TO_YEAR = .00273973
 date_format = '%m/%d/%Y'
 current_date = datetime.strptime(date.today().strftime(date_format), date_format)
 purchase_date = datetime.strptime(purchase_date, date_format)
 date_difference = (current_date - purchase_date).days * DAY_TO_YEAR
 current_price = (current_price)
 purchase_price = (purchase_price)
 stock_value_difference = current_price - purchase_price
 return '{0:.2f}%'.format(((stock_value_difference / purchase_price) / date_difference) * 100)


#End of program    
# -======================================================================