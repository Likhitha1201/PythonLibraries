""" 
    @Author: Likhitha S
    @Date: 21-10-2024 17:30
    @Last Modified by: Likhitha S
    @Last Modified time: 21-10-2024 17:30
    @Title:Write a Python programming to display a bar chart of the popularity of programming 
    Languages. Specify the position of each bar plot.  

"""
import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to draw a bar graph by specifying the position.
        Parameters: 
            prg_lang, popularity are the list of points that as to be displayed on graph.
        return:
            It displays the bar graph with position.

    """
    
    prg_lang=np.array(['java', 'python', 'PHP','javascript','c#','c++'])
    popularity= np.array([22.2,17.6,8.8,8,7.7,6.7])
    positions=np.arange(len(prg_lang))
    plt.bar(positions, popularity, align='center', alpha=0.7, color='lightgreen')
    plt.xticks(positions, prg_lang)
    plt.title("Programming Languages")
    plt.xlabel("popularity (%)")
    plt.ylabel("popularity of programming language")
    plt.show()
   
if __name__=="__main__":
    main()