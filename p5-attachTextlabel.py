""" 
    @Author: Likhitha S
    @Date: 21-10-2024 17:30
    @Last Modified by: Likhitha S
    @Last Modified time: 21-10-2024 17:30
    @Title:Write a Python programming to display a bar chart of the popularity of programming Languages. 
    Attach a text label above each bar displaying its popularity (float value).  

"""
import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to draw a bar graph with text plot.
        Parameters: 
            prg_lang, popularity are the list of points that as to be displayed on graph.
        return:
            It displays the bar graph with text label on  each bar in a bar graph.

    """
    
    prg_lang=np.array(['java', 'python', 'PHP','javascript','c#','c++'])
    popularity= np.array([22.2,17.6,8.8,8,7.7,6.7])
    plt.bar(prg_lang, popularity)
    for i, value in enumerate(popularity):
        # plt.text(i, popularity[i], f'{value}', ha='center', va='bottom')
        plt.text(i, value + 0.3, f'{value}', ha='center')
        
    plt.title("Programming Languages")
    plt.xlabel("popularity (%)")
    plt.ylabel("popularity of programming language")
    plt.show()
   
if __name__=="__main__":
    main()