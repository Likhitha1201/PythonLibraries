""" 

    @Author: Likhitha S
    @Date: 20-10-2024 15:30
    @Last Modified by: Likhitha S
    @Last Modified time: 20-10-2024 15:30
    @Title: Write a Python program to plot two or more lines and set the line markers. 
 
      
           
"""

import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to ploat aline graph with different markers.
        Parameters: 
           x and y  are list of points that as to be displayed on graph.
        return:
            It displays the line graph with different markers.

    """
    
    x=np.array([2,3,5,6,0,1])
    y=np.array([0,1,4,5,2,3])
    plt.plot(x, marker='*')
    plt.plot(y, marker="o")

    plt.show()
    
if __name__=="__main__":
    main()
    