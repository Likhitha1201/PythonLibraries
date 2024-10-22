""" 
    @Author: Likhitha S
    @Date: 22-10-2024 12:40
    @Last Modified by: Likhitha S
    @Last Modified time: 22-10-2024 12:40
    @Title:Write a Python program to create bar plot from a DataFrame. 

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    """

        Description: 
            This function is used to plot a bar graph .
        Parameters: 
            data is the collection key-value pair.
        return:
            It displays the bar graph.

    """
    
    data={
       'a':[2,4,6,8,10] ,
       'b':[4,2,4,2,2],
       'c':[8,3,4,5,6],
       'd':[7,2,3,4,6],
       'e':[6,6,8,3,1]  
    }
    
    label=['a','b','c','d','e']
    arr=pd.DataFrame(data, index=label)
    arr.plot(kind='bar')
    plt.show()
    
if __name__=="__main__":
    main()