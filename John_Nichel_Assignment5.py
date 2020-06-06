"""
Created on Saturday May  2 22:44:23 2020
@author: Nichel Emmanuel
# Python Version: 3.7.7.
# Week 5 Programming Assignment: Using Classes
Functionality: The information in investor dictionary is put into the stock_ownership 
class along with the original functions turned into methods including 
calculations for the loss/gain, percent yield, and yearly earnings. 
A class is then created for investor infomation including address and phone number.
A third class is created for bonds that inherits the information from the stock class.
ID field is added to all three classes with investor_ID for the investor class and purchase_ID
for the stock and bond class.The classes are then instantiated with all the stock informationand a single bond is added.
A report then displays all the class and bond information with columns for stock, share#,
and earnings/loss to display stocks, and bond, quantity, and earnings/loss to display the one bond. 
"""

# Set up the stock data variables as class attributes and functions as stock class methods.class stock_ownership():
class stock_ownership():

    #fetching values for stock symbols,number of shares,purchase price, 
    #current price of the stock and purchase date.
    def __init__(self,stock_symbol,number_of_shares,stock_purchase_price,stock_current_value,stock_purchase_date):
        
        self.stock_symbol = stock_symbol
        self.number_of_shares = number_of_shares
        self.stock_purchase_price = stock_purchase_price
        self.stock_current_value = stock_current_value
        self.stock_purchase_date = stock_purchase_date
    
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
   
class Bond(stock_ownership):    
 
 def __init__(self,stock_symbol,number_of_shares,stock_purchase_price,stock_current_value, stock_purchase_date):        
      
        super().__init__(stock_symbol,number_of_shares,stock_purchase_price,stock_current_value, stock_purchase_date)        
        self.bond_coupon = 0.0      
        self.bond_yield = 0.0
       
       
#Creating the investor class
class Investor:
    
 #fetching values for name, address,and phone number
 def __init__(self,name,address, phone):

        self.name=name
        self.address = address
        self.phone = phone
       
       
#Below code holds values for stock symbols,
#shares count,purchase price, current price and purchase date.
        
purchase_ID1 = stock_ownership('GOOGL',125,772.88,941.53,'08/01/2015')
purchase_ID2 = stock_ownership('MSFT ',85,56.60,73.04,'08/01/2015')
purchase_ID3 = stock_ownership('RDS-A',400,49.58,55.74,'08/01/2015')
purchase_ID4 = stock_ownership('AIG  ',235,54.21,65.27,'08/01/2015')
purchase_ID5 = stock_ownership('FB   ',150,124.31,172.45,'08/01/2015')
purchase_ID6 = stock_ownership('M    ',425,30.30,23.98,'01/10/2017')
purchase_ID7 = stock_ownership('F    ',85,12.58,10.95,'02/17/2017')
purchase_ID8 = stock_ownership('IBM  ',80,150.37,145.30,'05/12/2017')

#input data for investor  (name,address,phone)
investor = Investor ('Bob Smith', '10400, PM DR', '123-456-7890')

#input data for Bond investment stock symbols,number of shares,purchase price, 
#current price of the stock and purchase date.
inverstor_bond = Bond ('GT2:GOV',200,100.02,100.05,'01/07/2017')

#Below are the dictionaries that holds values for stock symbols,shares count,
# purchase price and current price instanciated from purrchase_id distionary.
purchase_ID= [purchase_ID1,purchase_ID2,purchase_ID3,purchase_ID4,purchase_ID5,purchase_ID6,purchase_ID7,purchase_ID8]

''' Output Report '''
# Stock Ownership Report title with table column headings
#Below section print report for stocks owned
print('\n\nStock Ownership for Bob Smith')
print('------------------------------------------------\n')
print('STOCK              SHARE#                  EARNINGS/LOSS            YEARLY % EARNING/LOSS')
print('------------------------------------------------------------------------------------------------------')   

# For loop through list to output the data on each company to the report's detail lines  
for purchase in purchase_ID:
 #Below code displays the report of stocks and the total earnings of the investor. 
 print(purchase.stock_symbol + '               ' + str(purchase.number_of_shares) \
                      + '                      ' + str(purchase.calculate_earnings_loss()) \
                        + '                    ' + str(purchase.calculate_yearly_rate_earnings()))

print('------------------------------------------------------------------------------------------------------')   

#Below section print report for bond owned and its data.

print('\n\nBond Ownership for Bob Smith')
print('------------------------------------------------\n')

print('STOCK              SHARE#                  EARNINGS/LOSS            YEARLY % EARNING/LOSS')
print('------------------------------------------------------------------------------------------------------')   

#Below code displays the report of bonds and the total earnings of the investor. 
print(inverstor_bond.stock_symbol + '               ' + str(inverstor_bond.number_of_shares)
                         + '                      ' + str(inverstor_bond.calculate_earnings_loss()) 
                           + '                    ' + str(inverstor_bond.calculate_yearly_rate_earnings()))

#End of program    
# -======================================================================
