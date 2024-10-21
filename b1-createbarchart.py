""" 
    @Author: Likhitha S
    @Date: 18-10-2024 17:30
    @Last Modified by: Likhitha S
    @Last Modified time: 18-10-2024 17:30
    @Title:Write a Python programming to display a bar chart of the popularity of programming Languages.  

"""
import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to draw a bar graph for given plots.
        Parameters: 
            prg_lang, popularity are the list of points that as to be displayed on graph.
        return:
            It displays the bar graph.

    """
    
    prg_lang=np.array(['java', 'python', 'PHP','javascript','c#','c++'])
    popularity= np.array([22.2,17.6,8.8,8,7.7,6.7])
    
    plt.bar(prg_lang, popularity, color='aqua')
    plt.show()
   
if __name__=="__main__":
    main()