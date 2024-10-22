""" 
    @Author: Likhitha S
    @Date: 22-10-2024 17:30
    @Last Modified by: Likhitha S
    @Last Modified time: 22-10-2024 17:30
    @Title: Write a Python programming to create a pie chart of gold medal achievements of five most 
    successful countries in 2016 Summer Olympics. Read the data from a csv file.  

"""

import matplotlib.pyplot as plt
import pandas as pd

def main():
    """

        Description: 
            This function is used to draw a pie chart by reading it from csv file.
        Parameters: 
            Prog_lang, Popularity are the list of points and labels that as to be displayed on chart.
        return:
            It displays the labeled piechart.

    """
    
    data=pd.read_csv('samplepie.csv')
    plt.pie(data['gold_medal'], labels=data['country'], autopct="%1.1f%%", startangle=100)
    plt.title('Gold Medal Achievements in 2016 Summer Olympics', color='red', size=15)

    plt.show()
    
if __name__=="__main__":
    main()