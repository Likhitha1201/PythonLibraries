""" 

    @Author: Likhitha S
    @Date: 20-10-2024 15:30
    @Last Modified by: Likhitha S
    @Last Modified time: 20-10-2024 15:30
    @Title:Write a Python program to plot two or more lines with different styles.
 
      
           
"""

import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to ploat aline graph with different styles.
        Parameters: 
           x and y  are list of points that as to be displayed on graph.
        return:
            It displays the line graph with different style.

    """
    x=[0,4,8,5,9]
    y=np.array([1,6,8,4,7])

    plt.plot(x, linestyle='dashed')
    plt.plot(y, ls='-.')

    plt.show()
    
if __name__=="__main__":
    main()
    