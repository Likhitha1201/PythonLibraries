""" 
    @Author: Likhitha S
    @Date: 18-10-2024 17:30
    @Last Modified by: Likhitha S
    @Last Modified time: 18-10-2024 17:30
    @Title:Write a Python program to draw a line with suitable label in the x axis, y axis and a title  
           
"""
import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to draw a labeled graph.
        Parameters: 
            x,y are the list of points that as to be displayed on graph.
        return:
            It displays the labeled line graph.

    """
    
    x=np.array([1,2,3,4])
    y=np.array([5,6,7,8])
    plt.plot(x,y)
    plt.title("Dissolved Oxygen Level")
    plt.xlabel("Average Oxygen")
    plt.ylabel("maximum cloride")
    
    plt.show()
    
   
if __name__=="__main__":
    main()