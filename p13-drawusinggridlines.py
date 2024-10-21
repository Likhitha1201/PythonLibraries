""" 

    @Author: Likhitha S
    @Date: 21-10-2024 13:30
    @Last Modified by: Likhitha S
    @Last Modified time: 21-10-2024 13:30
    @Title:  Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with linestyle -, width .5. and color blue. 

           
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    """

        Description: 
            This function is used to ploat a graph with gride lines with closing values.
        Parameters: 
           x, y0, y1 and y2  are list of points used to plota different types of graph
        return:
            It displays the graph.

    """
    
    data={
        'Date': ['03-10-16','04-10-16', '05-10-16', '06-10-16', '07-10-16'],
        'Close':[772.559998, 776.429993, 776.469971, 776.859985, 775.080017]
    }
    df= pd.DataFrame(data)
    # converting date column to datetime format
    df['Date']=pd.to_datetime(df['Date'], format='%d-%m-%y')
    plt.plot(df['Date'], df['Close'], marker='o', label="Closing value")
    plt.title('Alphabet Inc. between October 3, 2016 to October 7, 2016. ')
    plt.xlabel('Date with Time')
    plt.ylabel('Closing price (USD)')
    plt.grid(linestyle='dashed', color='b', linewidth=0.5,)
    plt.legend()
    plt.tight_layout() # it automatically adjust the subploting  to given specified padding
    plt.show()
    
if __name__=="__main__":
    main()
    