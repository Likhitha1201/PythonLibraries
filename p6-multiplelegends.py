""" 

    @Author: Likhitha S
    @Date: 20-10-2024 15:30
    @Last Modified by: Likhitha S
    @Last Modified time: 20-10-2024 15:30
    @Title:Write a Python program to plot two or more lines with legends, different widths and colors. 
 
      
           
"""

import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to ploat aline graph with legends.
        Parameters: 
           x and y  are list of points that as to be displayed on graph.
        return:
            It displays the labeled line graph as mentioned.

    """
    x= [2,4,6,8,10,12]
    y= [3,9,12,15,18,21]

    plt.plot(x, linewidth=2, c='g', label='2table')
    plt.plot(y, linewidth=2.5, color='c', label='3table')
    plt.title("Plotting multiple lines")
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend(title='different plots')
    
    plt.show()  
    
if __name__=="__main__":
    main()
    