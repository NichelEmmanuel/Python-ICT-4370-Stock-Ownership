'''
Stock and bond Info from a Text File and Output the Results to a Database
Created on Sunday May 18 22:44:23 2020
@author: Nichel Emmanuel
# Python Version: 3.7.7.
# Week 7 Programming Assignment
Description: The assignment utilizes previous Assignment 4 ,5 and 6, to set up code.
Reading the Stock and bond Info from a Text File and Output the Results to a Database 
The function module is combined with the original module. 
A report then displays all the class and bond information with columns for stock, share#, and 
earnings/loss to display stocks, and bond, quantity, and earnings/loss to display the one bond. 
'''


# Setup the stock data variables as class attributes and functions as stock class methods.class Stock():              

class CompanyStock():
    #fetching values for stock symbols,number of shares,purchase price, 
    #current price of the stock and purchase date.
    def __init__(self,stock_symbol,number_of_shares,purchase_price,current_value,purchase_date,purchase_ID,owner_ID):
        
        self.stock_symbol = stock_symbol
        self.number_of_shares = number_of_shares
        self.purchase_price = purchase_price
        self.current_value = current_value
        self.purchase_date = purchase_date
        self.purchase_ID = purchase_ID
        self.owner_ID = owner_ID
        
        
    def calculate_earnings_loss(self):
        #formula used = ((((current value – purchase price)/purchase price)/
        #              (current date – purchase date)))*100       
        #fucntion to Calculate yearly earnings/loss rate of stocks     
  
        calculate_earnings_loss = self.number_of_shares * (self.current_value - self.purchase_price)        
        return ("$" + format(calculate_earnings_loss, ',.2f'))
        
    def calculate_earnings_percentage(self):      
    #fucntion to calculate the earning or loss of stock.     
        return (self.current_value - self.purchase_price) / self.purchase_price
                
    def calculate_yearly_rate_earnings(self):
        from datetime import datetime        
        #fucntion to Calculate the percentage yield/loss for stocks
        days_interval = datetime.now() - datetime.strptime(self.purchase_date,"%m/%d/%Y")        
        return (self.calculate_earnings_percentage()/(days_interval.days/365))*100

#Below class is written to create a Bond. it holds value for Bond coupon and Bond yield
class CompanyBond():
	
    def __init__(self,bond_symbol,number_of_bonds,purchase_price,current_value,purchase_date,owner_ID,bond_ID,bond_coupon,bond_yield):
		
		#fetching values bond symbols,number of shares the investor owns,
        #purchase price of bond originally,current price of bond, and the original purchase date.
        
        self.bond_symbol = bond_symbol
        self.number_of_bonds = number_of_bonds
        self.purchase_price = purchase_price
        self.current_value = current_value
        self.purchase_date = purchase_date
        self.bond_coupon = bond_coupon
        self.bond_yield = bond_yield
        self.bond_ID = bond_ID
        self.owner_ID = owner_ID
        
    def calculate_earnings_loss(self):
        #fucntion to Calculate loss/gain for stocks     
        calculate_earnings_loss = self.number_of_bonds * (self.current_value - self.purchase_price)        
        return ("$" + format(calculate_earnings_loss, ',.2f'))
        
    def calculate_earnings_percentage(self):      
        #fucntion to Calculate the percentage yield/loss for stocks
        return (self.current_value - self.purchase_price) / self.purchase_price
                
    def calculate_yearly_rate_earnings(self):
        from datetime import datetime        
        #fucntion to Calculate yearly earnings/loss rate of stocks  
        days_interval = datetime.now() - datetime.strptime(self.puchase_date,"%m/%d/%Y")        
        return (self.calculate_earnings_percentage()/(days_interval.days/365))*100

        
#Creating the investor class
class owner:
    #setup values for the investor clas name, address,and phone number
	def _init_(self,owner_ID,name,address, phone):
	        #fetching values like owner_ID,name, address,and phone number for investor class
	        self.owner_ID = owner_ID
	        self.name = name
	        self.address = address
	        self.phone = phone

        
#Input section          
#Below code read values from  files  for stock symbols,
#shares count,purchase price, current price and purchase date.

# Exception handling for opening and reading the companies’ stock text file
try: 
     # Open stock text file and read file contents
     # Into a list of all the file’s line reacords
    stock_file_name = 'Lesson6_Data - Stocks.txt'
    with open('Lesson6_Data - Stocks.txt') as company_stock_file:
        company_stock_lines = company_stock_file.readlines()
except FileNotFoundError:
  # If the file does not exist , alert the user that the file was not found.
    print ('The stock file named   ' + stock_file_name + '   was not found.  \n')
else:
   print ('The stock file named    ' + stock_file_name + '   was opend.  \n')
   
   
# Exception handling for opening and reading the companies’ bond text file
try: 
     # Open bond text file and read file contents
     # Into a list of all the file’s line reacords
    bond_file_name = 'Lesson6_Data - Bond.txt'
    with open('Lesson6_Data - Bond.txt') as company_bond_file:
        company_bond_lines = company_bond_file.readlines()
except FileNotFoundError:
  # If the file does not exist , alert the user that the file was not found.
    print ('The Bond file named   ' + bond_file_name + '   was not found.  \n')
else:
   print ('The Bond file named    ' + bond_file_name + '   was opend.  \n')
   
#========================================================================================================================================


# Creating 8 company – stock Class instance (only one purchase per company in this case
# Populate each instance – member with data already read from the txt file 
# number the 8 companies from 0 to 7 , including this # in the purchase ID
#Initializing a list to holds 8 company classes – to enable loop-indexing 
#to avoid repetitive code starting with company 1 instead of company 0 , 
#since skipping the last 5 header lines 
company_stocks = [0,1,2,3,4,5,6,7,8]

for company_number in range (1,9):
      purchase_ID = "Bob_Smith_purchase_number_" + str(company_number)
      owner_ID = "1_Bob_Smith"
     # create and populate company stock class instances
      company_stocks[company_number] = CompanyStock(
                   company_stock_lines [ (company_number * 5) + 0 ].rstrip(),
                   company_stock_lines [ (company_number * 5) + 1 ].rstrip(),
                   company_stock_lines [ (company_number * 5) + 2 ].rstrip(),
                   company_stock_lines [ (company_number * 5) + 3 ].rstrip(),
                   company_stock_lines [ (company_number * 5) + 4 ].rstrip(),
                   purchase_ID,
                   owner_ID )
# Creating 1 company – bond Class instance

company_bond = [0,1]

for company_number in range (1,2):
      bond_ID = "Bob_Smith_purchase_number_" + str(company_number)
      owner_ID = "1_Bob_Smith"
     # create and populate company stock class instances
      company_bond[company_number] = CompanyBond(
                   company_bond_lines [ (company_number * 7) + 0 ].rstrip(),
                   company_bond_lines [ (company_number * 7) + 1 ].rstrip(),
                   company_bond_lines [ (company_number * 7) + 2 ].rstrip(),
                   company_bond_lines [ (company_number * 7) + 3 ].rstrip(),
                   company_bond_lines [ (company_number * 7) + 4 ].rstrip(),
                   company_bond_lines [ (company_number * 7) + 5 ].rstrip(),
                   company_bond_lines [ (company_number * 7) + 6 ].rstrip(),
                   bond_ID,
                   owner_ID )
#=============================================================================================
#Create a SQLite database
# Two tables – stock and bond

import sqlite3
database_path = 'Database_for_Stocks.sqlite'
#Establish a named connection to access the database 
conn = sqlite3.connect(database_path)
print ('\nCreated empty stocks database table layout')
#=====================================================
#write stock data to SQLite database
#First setup the database table layout 
sql_create_stock_table =''' CREATE TABLE IF NOT EXISTS     \
         company_stock_table (
                                                                
                                   Stock_symbol         text        NOT NULL, 
                                   number_of_shares     integer     NOT NULL,
				                   purchase_price       float       NOT NULL,
                                   current_value        float       NOT NULL,
                                   purchase_date        text        NOT NULL,
                                   purchase_ID          text        NOT NULL,
                                   Owner_ID             text        NOT NULL
                                   ); '''
#connect SQLite to the database
# located in the same directory as this python code file
connection = sqlite3.connect(database_path)
#Establish a named cursor to enable database commands
cursor = connection.cursor()

# use the table creation/layout above to set up the rows
cursor.execute(sql_create_stock_table)
#-------
connection.commit()
connection.close()
#==================================================================
#write stock data rows to the database
#from the company stock Classes
# start by re-connecting to the database
connection = sqlite3.connect(database_path)
cursor = connection.cursor()
# build the SQLite command to insert a row – record
# to pass to sqlite3 , including the name of the table
for company_number in range(1,9):
      cursor.execute('INSERT INTO company_stock_table VALUES(?,?,?,?,?,?,?)',
                 (company_stocks[company_number].stock_symbol,\
                  company_stocks[company_number].number_of_shares,\
                  company_stocks[company_number].purchase_price,\
                  company_stocks[company_number].current_value,\
                  str(company_stocks[company_number].purchase_date),\
                  str(company_stocks[company_number].purchase_ID),\
                  str(company_stocks[company_number].owner_ID)))\
#================================================================================
connection.commit()
connection.close()

#================================================================================
#Create a SQLite database
# bond table created

import sqlite3
database_path = 'Database_for_bond.sqlite'
#Establish a named connection to access the database 
conn = sqlite3.connect(database_path)
print ('\nCreated empty bond database table layout')
#=========================================================
#write bond data to SQLite database
#First setup the database table layout 
sql_create_bond_table =''' CREATE TABLE IF NOT EXISTS     \
         company_bond_table (
                                                                
                                   Bond_symbol          text        NOT NULL, 
                                   number_of_shares     integer     NOT NULL,
				                   purchase_price       float       NOT NULL,
                                   current_value        float       NOT NULL,
                                   purchase_date        text        NOT NULL,
                                   bond_coupon         integer      NOT NULL,
                                   bond_yield          integer     NOT NULL,
                                   bond_ID             text        NOT NULL,                   
                                   Owner_ID            text        NOT NULL
                                   
                                   ); '''
#connect SQLite to the database
# located in the same directory as this python code file
connection = sqlite3.connect(database_path)
#Establish a named cursor to enable database commands
cursor = connection.cursor()

# use the table creation/layout above to set up the rows
cursor.execute(sql_create_bond_table)
#-------
connection.commit()
connection.close()
#==================================================================
#write bond data rows to the database
#from the company bond Classes
# start by re-connecting to the database
connection = sqlite3.connect(database_path)
cursor = connection.cursor()
# build the SQLite command to insert a row – record
# to pass to sqlite3 , including the name of the table
for company_number in range(1,2):
      cursor.execute('INSERT INTO company_bond_table VALUES(?,?,?,?,?,?,?,?,?)',
                 (company_bond[company_number].bond_symbol,\
                  company_bond[company_number].number_of_bonds,\
                  company_bond[company_number].purchase_price,\
                  company_bond[company_number].current_value,\
                  str(company_bond[company_number].purchase_date),\
                  company_bond[company_number].bond_coupon,\
                  company_bond[company_number].bond_yield,\
                  str(company_bond[company_number].bond_ID),\
                  str(company_bond[company_number].owner_ID)))\
                  
#================================================================================
connection.commit()
connection.close()

#================================================================================

#Create a SQLite database
# table Owner

import sqlite3
database_path = 'Database_for_Owner.sqlite'
#Establish a named connection to access the database 
conn = sqlite3.connect(database_path)
print ('\nCreated empty owners database table layout')
#=============================================================================
#write stock data to SQLite database
#First setup the database table layout 
sql_create_owner_table =''' CREATE TABLE IF NOT EXISTS     \
         company_owner_table (
                                                                
                                    
				                   Owner_ID             text        NOT NULL,
                                   Name                 text        NOT NULL,
                                   Address              text        NOT NULL,
                                   Phone                integer     NOT NULL
                                   
                                   ); '''
                                   
#connect SQLite to the database
# located in the same directory as this python code file
connection = sqlite3.connect(database_path)
#Establish a named cursor to enable database commands
cursor = connection.cursor()

# use the table creation/layout above to set up the rows
cursor.execute(sql_create_owner_table)
#-------
connection.commit()
connection.close()
#========================================================================================
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute('INSERT INTO company_owner_table VALUES(?,?,?,?)',
                 (str ('1_Bob_Smith'),str ('Bob Smith'),str ('Newyork'),str (72098760)))\
                 
#=========================================================================================
connection.commit()
connection.close()

#=================================================================
#connect the program to the database to read from db to NEW classes – and print
import sqlite3
db_connection = sqlite3.connect('Database_for_stocks.sqlite')
cursur = db_connection.cursor()
#==========================================================================
#==========================================================================
#connect the program to the database
import sqlite3
db_connection = sqlite3.connect('Database_for_stocks.sqlite')
cursor = db_connection.cursor()
#==========================================================================

#==========================================================================
# Define Stock class
class NewCompanyStock():
    def __init__(self,stock_symbol,number_of_shares,purchase_price,current_value,purchase_date,purchase_ID,owner_ID):
        
        self.stock_symbol = stock_symbol
        self.number_of_shares = number_of_shares
        self.purchase_price = purchase_price
        self.current_value = current_value
        self.purchase_date = purchase_date
        self.purchase_ID = purchase_ID
        self.owner_ID = owner_ID
        
        
    def calculate_earnings_loss(self):
        #fucntion Calculate loss/gain for stocks
        calculate_earnings_loss = self.number_of_shares * (self.current_value - self.purchase_price)        
        return ("$" + format(calculate_earnings_loss, ',.2f'))
        
    def calculate_earnings_percentage(self):      
        #function to Calculate the percentage yield/loss for stocks
        return (self.current_value - self.purchase_price) / self.purchase_price
                
    def calculate_yearly_rate_earnings(self):
        from datetime import datetime        
        #function to Calculate yearly earnings/loss rate of stocks  
        days_interval = datetime.now() - datetime.strptime(self.purchase_date,"%m/%d/%Y")        
        return (self.calculate_earnings_percentage()/(days_interval.days/365))*100
             
       
#==============================================================================================================================
new_company_stocks = [0,1,2,3,4,5,6,7,8]
company_number = 1
for company_stock_record in cursor.execute('SELECT * FROM company_stock_table;'):
# Read in the table row record fields - into new Class instance 
 new_company_stocks[company_number] = NewCompanyStock(
	                  str(company_stock_record[0]),
	                  company_stock_record[1],
	                  company_stock_record[2],
	                  company_stock_record[3],
	                  company_stock_record[4],
	                  str(company_stock_record[5]),
	                  str(company_stock_record[6]))
	                  
 company_number = company_number + 1
 
#output report for stock ownership
#==========================================================================
print("\nStock Ownership for Bob Smith")
print('------------------------------------------------\n')
print('STOCK           SHARE#          EARNINGS/LOSS           YEARLY % EARNING/LOSS')
print('-----------------------------------------------------------------------------') 
#(Note that range from 1 to 9 gives company indexs from 1 to 8 )
for company_number in range(1,9):
 print(new_company_stocks[company_number].stock_symbol + "\t\t" +
       str(new_company_stocks[company_number].number_of_shares) + "\t\t" + 
       str(new_company_stocks[company_number].calculate_earnings_loss()) + "\t\t" +
       str(new_company_stocks[company_number].calculate_yearly_rate_earnings()))

db_connection.commit()
db_connection.close()
#==========================================================================
#==========================================================================
#connect the program to the database
import sqlite3
db_connection = sqlite3.connect('Database_for_bond.sqlite')
cursor = db_connection.cursor()
#==========================================================================

#==========================================================================
# Define Bond class
class NewCompanyBond():
	
    def __init__(self,bond_symbol,number_of_bonds,purchase_price,current_value,purchase_date,owner_ID,bond_ID,bond_coupon,bond_yield):
		
       
        self.bond_symbol = bond_symbol
        self.number_of_bonds = number_of_bonds
        self.purchase_price = purchase_price
        self.current_value = current_value
        self.purchase_date = purchase_date
        self.bond_coupon = bond_coupon
        self.bond_yield = bond_yield
        self.bond_ID = bond_ID
        self.owner_ID = owner_ID
        
    def calculate_earnings_loss(self):
        #function to Calculate loss/gain for Bonds  
        calculate_earnings_loss = self.number_of_bonds * (self.current_value - self.purchase_price)        
        return ("$" + format(calculate_earnings_loss, ',.2f'))
        
    def calculate_earnings_percentage(self):      
         #function to Calculate the percentage yield/loss for Bonds 
        return (self.current_value - self.purchase_price) / self.purchase_price
                
    def calculate_yearly_rate_earnings(self):
        from datetime import datetime
         #function to Calculate yearly earnings/loss rate of Bonds    
        days_interval = datetime.now() - datetime.strptime(self.purchase_date,"%m/%d/%Y")        
        return (self.calculate_earnings_percentage()/(days_interval.days/365))*100

       
#============================================================================================================
new_company_bonds = [0,1]
comp_number = 1
for company_bond_record in cursor.execute('SELECT * FROM company_bond_table;'):
# Read in the table row record fields - into new Class instance 
 new_company_bonds[comp_number] = NewCompanyBond(
                      str(company_bond_record[0]),
	                  company_bond_record[1],
	                  company_bond_record[2],
	                  company_bond_record[3],
	                  company_bond_record[4],
	                  str(company_bond_record[5]),
	                  str(company_bond_record[6]),
	                  company_bond_record[7],
	                  company_bond_record[8])
#output report for bonfs ownership             	                    
#=========================================================
print("\nBond Ownership for Bob Smith")
print('------------------------------------------------\n')
print('Bond          QUANTITY          EARNINGS/LOSS           YEARLY % EARNING/LOSS')
print('-----------------------------------------------------------------------------') 
print(new_company_bonds[comp_number].bond_symbol + "\t\t" + 
      str(new_company_bonds[comp_number].number_of_bonds) + "\t\t" 
      + str(new_company_bonds[comp_number].calculate_earnings_loss()) + "\t\t\t" 
      + str(new_company_bonds[comp_number].calculate_yearly_rate_earnings()))


db_connection.commit()
db_connection.close()
#===========================================================
# End of the Program.')

		
     
                 

