'''
Read JSON Data and Create Stock Data Graphs
Created on Sunday May 25 22:44:23 2020
@author: Nichel Emmanuel
# Python Version: 3.7.7.
# Week 8 Programming Assignment
Description: The assignment reading the Stock Info from a JSON File and
Output the Results in a graphical form. 
The graph shows the dates on the x-axis and the closing price on y-axis.
Given that the value of Google is so high, the other lines of the graph may appear fairly flat and low.
'''

#to read data from JSON file
import json
# matplotlib function to generate graph
import matplotlib.pyplot as plt

#flush dictionary to store the data
stocks = {} 
file = "AllStocks.json"

with open(file) as f:
    stocks = json.load(f) #loaded data into the stocks dictionary
    

#Creating the dates and prices list for each type of stock

#AIG stock dates
aig_dates = []
aig_prices = []
for i in stocks:
    if i['Symbol']=='AIG':
        aig_dates.append(i['Date'])
        aig_prices.append(i['Close'])

#Rearranging the dates from oldest to newest:        
aig_dates = aig_dates[::-1]      
aig_prices = aig_prices[::-1]
        
#F stocks  
F_dates = []
F_prices = []
for i in stocks:
    if i['Symbol']=='F':
        F_dates.append(i['Date'])
        F_prices.append(i['Close'])  
        
F_dates = F_dates[::-1]      
F_prices = F_prices[::-1]


#Facebook stock dates   
FB_dates = []
FB_prices = []
for i in stocks:
    if i['Symbol']=='FB':
        FB_dates.append(i['Date'])
        FB_prices.append(i['Close'])
        
FB_dates = FB_dates[::-1]      
FB_prices = FB_prices[::-1]

#GOOG stock dates 
GOOG_dates = []
GOOG_prices = []
for i in stocks:
    if i['Symbol']=='GOOG':
        GOOG_dates.append(i['Date'])
        GOOG_prices.append(i['Close'])
        
GOOG_dates = GOOG_dates[::-1]      
GOOG_prices = GOOG_prices[::-1]

#IBM stock dates   
IBM_dates = []
IBM_prices = []
for i in stocks:
    if i['Symbol']=='IBM':
        IBM_dates.append(i['Date'])
        IBM_prices.append(i['Close'])
        
IBM_dates = IBM_dates[::-1]      
IBM_prices = IBM_prices[::-1]

#M stock dates 
M_dates = []
M_prices = []
for i in stocks:
    if i['Symbol']=='M':
        M_dates.append(i['Date'])
        M_prices.append(i['Close'])
        
M_dates = M_dates[::-1]      
M_prices = M_prices[::-1]

#MSFT  stock dates       
MSFT_dates = []
MSFT_prices = []
for i in stocks:
    if i['Symbol']=='MSFT':
        MSFT_dates.append(i['Date'])
        MSFT_prices.append(i['Close'])
        
MSFT_dates = MSFT_dates[::-1]      
MSFT_prices = MSFT_prices[::-1]

#RDSA stock dates       
RDSA_dates = []
RDSA_prices = []
for i in stocks:
    if i['Symbol']=='RDS-A':
        RDSA_dates.append(i['Date'])
        RDSA_prices.append(i['Close'])
        
RDSA_dates = RDSA_dates[::-1]      
RDSA_prices = RDSA_prices[::-1]


#creating dates to show in the graph
dates = [GOOG_dates[0], GOOG_dates[50], GOOG_dates[100],
         GOOG_dates[150],GOOG_dates[200], GOOG_dates[250], 
         GOOG_dates[300], GOOG_dates[350],GOOG_dates[400],
         GOOG_dates[450],GOOG_dates[-1]]


plt.rcParams["figure.figsize"] = (10,3)
plt.title("Historical Stock Data")
plt.xlabel('Stock Valuation Dates')
plt.ylabel('Stock Closing Prices in Dollars')
plt.plot(aig_dates, aig_prices, label="AIG")
plt.plot(F_dates, F_prices, label="F")
plt.plot(FB_dates, FB_prices, label="FB")
plt.plot(GOOG_dates, GOOG_prices,label="GOOG")
plt.plot(IBM_dates, IBM_prices,label="IBM")
plt.plot(M_dates, M_prices,label="M")
plt.plot(MSFT_dates, MSFT_prices,label="MSFT")
plt.plot(RDSA_dates, RDSA_prices, label="RDSA")
plt.xticks(dates, rotation=45) 
plt.legend()
plt.show()
