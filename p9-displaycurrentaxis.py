""" 

    @Author: Likhitha S
    @Date: 20-10-2024 15:30
    @Last Modified by: Likhitha S
    @Last Modified time: 20-10-2024 15:30
    @Title: Write a Python program to display the current axis limits values and set new axis values.
      
           
"""

import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to ploat aline graph with changing to new axis limits.
        Parameters: 
           x and y  are list of points that as to be displayed on graph.
        return:
            It displays the line graph and current and new axis limits.

    """
    
   
    x=np.array([1, 2, 3, 4, 5])
    y=np.array([2, 4, 6, 8, 10])
    plt.plot(x, y)
    
    # to know the current axis's plot points
    current_plot=plt.axis()
    print(f" current axis plotting limits are: {current_plot}")

    # to set new axis's plot points
    plt.axis([0,6,0,12])
    new_plot= plt.axis()
    print(f" new axis plotting are: {new_plot}")
    plt.grid()
    plt.show()
    
if __name__=="__main__":
    main()
    