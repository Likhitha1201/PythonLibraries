""" 

    @Author: Likhitha S
    @Date: 20-10-2024 15:30
    @Last Modified by: Likhitha S
    @Last Modified time: 20-10-2024 15:30
    @Title: Write a Python program to plot two or more lines on same plot with suitable legends of each line. 
      
           
"""

import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to ploat aline graph with two plots in the same graph.
        Parameters: 
            data is the dictionary that contains list of points that as to be displayed on graph.
        return:
            It displays the labeled line graph as mentioned.

    """
    x=[0, 2, 4, 6, 8, 10]
    y1=[1, 3, 6, 9, 12, 15]
    y2=[1, 5, 10, 15, 20, 25]
    
    plt.plot(x, y1, label='three tables', color='maroon')
    plt.plot(x, y2, label= "Five Tables", color='g')
    plt.title("Multiple Line plotting's")
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    plt.grid()
    plt.show()    
    
if __name__=="__main__":
    main()
    