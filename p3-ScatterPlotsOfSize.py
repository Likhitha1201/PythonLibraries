""" 
    @Author: Likhitha S
    @Date: 23-10-2024 9:40
    @Last Modified by: Likhitha S
    @Last Modified time: 23-10-2024 9:40
    @Title: Write a Python program to draw a scatter plot comparing two subject marks of Mathematics 
    and Science. Use marks of 10 students. 
       
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
    
    math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34] 
    science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30] 
    marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
    plt.scatter(math_marks, science_marks, marker='x', color='green', alpha=0.7)
    plt.title("Comparision of maths and science marks", size=15, color='r')
    plt.xlabel("mathematics marks", size=12)
    plt.ylabel("science marks", size=12)
    plt.xticks(marks_range)
    plt.yticks(marks_range)
    
    plt.show()
   
if __name__=="__main__":
    main()