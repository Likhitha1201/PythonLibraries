""" 

    @Author: Likhitha S
    @Date: 23-10-2024 9:55
    @Last Modified by: Likhitha S
    @Last Modified time: 23-10-2024 9:55
    @Title: Write a Python program to draw a scatter plot for three different groups camparing weights 
    and heights.  
       
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    """

        Description: 
            This function is used to draw a scatter graph by comparing the marks of the two subjects.
        Parameters: 
           math_marks, science_marks and marks_range are the given plots.
        return:
            It displays the graph with scatter plots.

    """
    
    x_weight = np.random.rand(50)
    x_height = np.random.rand(50)
    y_weight = np.random.rand(50)
    y_height = np.random.rand(50)
    z_weight = np.random.rand(50)
    z_height = np.random.rand(50)
    
    plt.scatter(x_weight, x_height, label='group1', color='g')
    plt.scatter(y_weight, y_height, label='group2', color='y')
    plt.scatter(z_weight, z_height, label='group3', color='pink')
    
    plt.title("Comparision Of Group's Hight and Weight", color= 'r', size=15)
    plt.xlabel("Group's Weights", color= 'r', size=12)
    plt.ylabel("Group's Height", color= 'r', size=12)
    plt.legend()
    plt.grid()
    
    plt.show()
   
if __name__=="__main__":
    main()