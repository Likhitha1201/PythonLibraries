""" 
    @Author: Likhitha S
    @Date: 18-10-2024 15:30
    @Last Modified by: Likhitha S
    @Last Modified time: 18-10-2024 15:30
    @Title: Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016.  
           
"""

import matplotlib.pyplot as plt
import pandas as pd

def main():
    """

        Description: 
            This function is used to draw a labeled graph reading from test.txt file.
        Parameters: 
            data is the dictionary that contains list of points that as to be displayed on graph.
        return:
            It displays the labeled line graph as mentioned.

    """
    
    data=pd.read_csv("fdata.csv", parse_dates=['Date'], dayfirst=True)
    data.columns = data.columns.str.strip()
    # strip() helps to remove unwanted spaces. and finally the cleaned ones will be updated in data.columns
    
    print(data.head())
    print(data.columns)
    
    data.set_index('Date', inplace=True )
    plt.figure(figsize=(10,6))
    # here, date is taken as data.index
    plt.plot(data.index, data['Open'], label="Open", marker='o', c='b')
    plt.plot(data.index, data['High'], label='High', marker='o', c='g')
    plt.plot(data.index, data['Low'],  label='Low', marker='o', c='y')
    plt.plot(data.index, data['Close'],label='Close', marker='o', c='m')
    
    plt.title("Financial Data of Alphabet Inc (Oct 3, 2016 - Oct 7, 2016)",c='r')
    plt.xlabel('Date')
    plt.ylabel("Price(USD)")
    # plt.tight_layout()-- it helps in automatically adjust spacing between the subplots.
    plt.tight_layout()
    plt.grid()
    plt.show()
    
if __name__=="__main__":
    main()