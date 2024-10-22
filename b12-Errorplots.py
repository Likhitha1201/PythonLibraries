""" 
    @Author: Likhitha S
    @Date: 22-10-2024 12:40
    @Last Modified by: Likhitha S
    @Last Modified time: 22-10-2024 12:40
    @Title:Write a Python program to create bar plots with error bars on the same figure. 

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    """

        Description: 
            This function is used to plot a bar graph with error bars .
        Parameters: 
            x,y,z are the the plot points that are used to draw the graph.
        return:
            It displays the bar graph.

    """
    z=['a','b','c','d','e']
    x=[0, 2, 4, 6, 8]
    y=[1, 7, 3, 9, 5]
    plt.bar(z, x, yerr=y, color='palegreen', capsize=5)
    plt.xlabel("Even numbers")
    plt.ylabel("Odd numbers")
    plt.title("ploting plots of even and odd numbers")
    plt.tight_layout()
    plt.show()
    
if __name__=="__main__":
    main()