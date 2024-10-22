""" 
    @Author: Likhitha S
    @Date: 22-10-2024 12:40
    @Last Modified by: Likhitha S
    @Last Modified time: 22-10-2024 12:40
    @Title:  Write a Python programming to display a bar chart of the popularity of programming Languages. Increase bottom margin.  

"""
import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to bar graph with bottom margin of 0.3.
        Parameters: 
            prg_lang, popularity are the list of points that as to be displayed on graph.
        return:
            It displays the bar graph.

    """
    
    prg_lang=np.array(['java', 'python', 'PHP','javascript','c#','c++'])
    popularity= np.array([22.2,17.6,8.8,8,7.7,6.7])
    
    plt.bar(prg_lang, popularity)
    plt.subplots_adjust(bottom=0.3)
    plt.title("Programming Languages")
    plt.xlabel("popularity (%)")
    plt.ylabel("popularity of programming language")
    plt.show()
   
if __name__=="__main__":
    main()