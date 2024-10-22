""" 

    @Author: Likhitha S
    @Date: 21-10-2024 13:30
    @Last Modified by: Likhitha S
    @Last Modified time: 21-10-2024 13:30
    @Title: Write a Python program to plot several lines with different format styles in one command using arrays.  

           
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
    
    x = np.array([0,2,4,6,8])
    y0 = [1, 2, 3, 4, 5]
    y1 = [2, 4, 6, 8, 10]
    y2 = [3, 5, 7, 9, 6]
    # plt.plot(x, y0, linestyle="dashed", c='g')
    # plt.plot(x, y1, ls='dotted', c='y')
    # plt.plot(x, y2, ls='-.', color='m')
    plt.plot(x, y0, 'r--', label='dashed lines')
    plt.plot(x, y1, 'g:', label='dotted lines')
    plt.plot(x, y2, 'y-', label='normal line')
    plt.title("multiple lines with different styles")
    plt.xlabel("x plotting styles")
    plt.ylabel("y plotting styles")

    plt.show()
    
if __name__=="__main__":
    main()
    