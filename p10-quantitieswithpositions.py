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
            This function is used to ploat aline graph with quantities of positiona x and y.
        Parameters: 
           x and y  are list of points that as to be displayed on graph.
        return:
            It displays the line graph.

    """
    
   
    x=np.array([1, 2, 3, 4, 5])
    y=np.array([2, 4, 6, 8, 7])
    plt.plot(x, y)
    plt.title("plot of quantities at x and y position's")
    plt.xlabel("x position")
    plt.ylabel("y position") 
   
    plt.show()
    
if __name__=="__main__":
    main()
    