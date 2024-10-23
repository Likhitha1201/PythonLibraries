""" 
    @Author: Likhitha S
    @Date: 23-10-2024 9:00
    @Last Modified by: Likhitha S
    @Last Modified time: 23-10-2024 9:00
    @Title:Write a Python program to draw a scatter graph taking a random distribution in X and Y and 
    plotted against each other.  
"""
import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to draw a scatter graph.
        Parameters: 
            x, y are the plots taken from the random.randint()
        return:
            It displays the graph with scatter plots.

    """
    
    x=np.random.rand(1, 10, 50)
    y=np.random.rand(1, 10, 50)
   
    plt.scatter(x, y, marker='x', color='g')
    plt.title("Scatter plot of random values", size=15, color='r')
    plt.xlabel("x-values", size=12)
    plt.ylabel("y-values", size=12)
    
    plt.show()
   
if __name__=="__main__":
    main()