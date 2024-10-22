""" 
    @Author: Likhitha S
    @Date: 22-10-2024 12:20
    @Last Modified by: Likhitha S
    @Last Modified time: 22-10-2024 12:20
    @Title: Write a Python programming to display a bar chart of the popularity of programming 
    Languages. Select the width of each bar and their positions. 

"""
import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to selectg the width and position of each bar.
        Parameters: 
            prg_lang, popularity are the list of points that as to be displayed on graph.
        return:
            It displays the bar graph with.

    """
    
    prg_lang=np.array(['java', 'python', 'PHP','javascript','c#','c++'])
    popularity= np.array([22.2,17.6,8.8,8,7.7,6.7])
    widths=[0.5, 0.3, 0.4, 0.8, 0.3, 0.5]
    positions=[i for i in range(len(prg_lang))]
    plt.bar(positions, popularity, align='center', alpha=0.7, color='lightgreen', width=widths)
    plt.xticks(positions, prg_lang)
    plt.title("Programming Languages")
    plt.xlabel("popularity (%)")
    plt.ylabel("popularity of programming language")
    plt.show()
   
if __name__=="__main__":
    main()