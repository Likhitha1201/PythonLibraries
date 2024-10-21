""" 
    @Author: Likhitha S
    @Date: 18-10-2024 17:50
    @Last Modified by: Likhitha S
    @Last Modified time: 18-10-2024 17:50
    @Title:Write a Python program to draw a line using given axis values taken from a text file, with suitable label in the x axis, y axis and a title. 

           
"""
import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to draw a labeled graph reading from test.txt file.
        Parameters: 
            x,y are the list of points that as to be displayed on graph.
        return:
            It displays the labeled line graph.

    """
    
    import matplotlib.pyplot as plt

    file=open('test.txt','r')
    # Read data from file
    x_values = []
    y_values = []

    for line in file:
        x, y = map(int, line.split())
        x_values.append(x)
        y_values.append(y)

    print('values of x:',x_values)
    print('values of y:',y_values)
    # Plotting the line
    plt.plot(x_values, y_values, marker='o')

    # Labels and title
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Line Plot from test file')

    # Display the plot
    plt.show()

    
   
if __name__=="__main__":
    main()