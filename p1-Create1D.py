
""" 
    @Author: Likhitha S
    @Date: 13-10-2024 13:40
    @Last Modified by: Likhitha S
    @Last Modified time: 13-10-2024 13:40
    @Title: Write a Python program to create and display a one-dimensional array-like object containing an array of data using Pandas module.  
           
"""

import pandas as pd

def main():
    """

        Description: 
            This function is used to create 1D-array.
        Parameters: 
            data is used to store the elements in 1D-array .
        return:
            It print the array elements.

    """
    
    
    data=[12,23,45,67,48,96,99]
    result=pd.Series(data)
    print(result)
    print('--or--')
    
    res=pd.Series([12,13,14,15,16])
    print(res)
    
if __name__=="__main__":
    main()