""" 

    @Author: Likhitha S
    @Date: 21-10-2024 13:30
    @Last Modified by: Likhitha S
    @Last Modified time: 21-10-2024 13:30
    @Title:  Write a Python program to create multiple types of charts 

           
"""

import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to ploat a different type of charts.
        Parameters: 
           x, y0, y1 and y2  are list of points used to plota different types of graph
        return:
            It displays all types of graph.

    """
    
    x=np.array(['A', 'B', 'C', 'D', 'E'])
    y0=[12,14,15,16,17]# for line plottings
    y1=[10,20,30,40,25] # for bar graph
    y2=[25,35,10,49,18] # for piechart
    
    print('--line plot---')
    #plt.figure(figsize=(2,10)) # it helps to specify the width and height for all charts.
    #plot1
    plt.subplot(1,3,1)
    plt.plot(x,y0, color='g')
    plt.title("LineChart")
    plt.xlabel("Categories")
    plt.ylabel("values")
    plt.grid(c='lightgrey')
   
    print('---bar graph---')
    #plot2
    plt.subplot(1,3,2)
    plt.bar(x,y1)
    plt.title("Bar Chart")
    plt.xlabel('Categories')
    plt.ylabel('values')
    plt.grid(c='lightgrey')

    print("---pie chart---")
    #plot3
    plt.subplot(1,3,3)
    c=['pink','c','lightgreen','aqua','m']
    plt.pie(y2, labels=x, colors=c)
    plt.title("Pie Chart")
    plt.suptitle("Different types of charts are:", color='k', size=20)
    
    plt.show()
    
if __name__=="__main__":
    main()
    