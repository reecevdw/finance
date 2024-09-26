# import modules 
from pandas_datareader import data as pdr 
import matplotlib.pyplot as plt 

# initializing Parameters 
start = "2020-01-01"
end = "2024-01-01"
symbols = ["TQQQ"] 

# Getting the data 
data = pdr.get_data_yahoo(symbols, start, end) 

# Display 
plt.figure(figsize = (20,10)) 
plt.title('Opening Prices from {} to {}'.format(start, end)) 
plt.plot(data['Open']) 
plt.show()
