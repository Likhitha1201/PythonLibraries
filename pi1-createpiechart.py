""" 
    @Author: Likhitha S
    @Date: 22-10-2024 17:30
    @Last Modified by: Likhitha S
    @Last Modified time: 22-10-2024 17:30
    @Title:  Write a Python programming to create a pie chart of the popularity of programming Languages.

"""
import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to draw a pie chart.
        Parameters: 
            x,y are the list of points that as to be displayed on graph.
        return:
            It displays the labeled piechart.

    """
    
    Prog_lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'] 
    Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
   
    plt.pie(Popularity, labels=Prog_lang)
    plt.title("Popularity Of Programming Languages")
    plt.show()
    
if __name__=="__main__":
    main()