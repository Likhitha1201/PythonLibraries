""" 
    @Author: Likhitha S
    @Date: 22-10-2024 16:20
    @Last Modified by: Likhitha S
    @Last Modified time: 22-10-2024 16:20
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
   
    x_mean=[0, 2, 4, 6, 8]
    y_deviation=[1, 7, 3, 9, 5]
    label=[int(i) for i in x_mean]
    width=0.35
    
    z=np.arange(len(x_mean))
    fig, var= plt.subplots()
    bars= var.bar(z, x_mean, width, yerr=y_deviation, capsize=5, edgecolor='k')
    
    for bar, value in zip(bars, label):
        var.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(value), 
                 ha='center', va='bottom', fontsize=10)
    # bar.get_x() is not constant, where it returns the co-ordinates of the lower-left corner of each individual bar in bar chart.
    
    # for i, bar in enumerate(bars):
    #     var.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(label[i]), 
    #              ha='center', va='bottom', fontsize=10)
        
        
        
    var.set_title("Even And Odd Numbers")
    var.set_ylabel("Odd Numbers")
    
    var.set_xticks(z)
    var.set_xticklabels([f"Bar{i+1}" for i in z])
    
    plt.tight_layout()
    
    plt.show()
    
if __name__=="__main__":
    main()