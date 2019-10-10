from forex_python.converter import CurrencyRates
import pandas as pd
import datetime	
from datetime import datetime

# Filename
filename = "bank_statement_sample.csv"

# Currency involved
currencyFROM = 'SGD'
currencyTO = 'IDR'

# Reading the CSV (Make sure it's in the same folder)
df = pd.read_csv(filename)
date_list = df['*Date'].tolist() # Convert data frame to list of dates
SGD_list = df['SGD'].tolist() # Convert SGD to list of SGDs

# Execute the currency exchange
c = CurrencyRates()
print ("There are a total of %i data points." %len(date_list))
for row in range(len(date_list)):
        row_date = date_list[row]
        row_SGD = SGD_list[row]
        date_obj = datetime.strptime(str(date_list[row]),"%d/%m/%y") # convert string to datetime
        rate = c.get_rate(currencyFROM, currencyTO, date_obj) # get the exchange rate
        print (row_SGD*rate)


# Getting syntax of time format
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
	

