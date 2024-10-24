""" 

    @Author: Likhitha S
    @Date: 24-10-2024 17:50
    @Last Modified by: Likhitha S
    @Last Modified time: 24-10-2024 17:50
    @Title:Write a program to draw bar plot of sex against survived for a dataset given in the url 
    https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv 
   
     
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():
    """

        Description: 
            This function is used to draw a graph.
        Parameters: 
            url is the input where we are going to get the dataset.
        return:
            It displays the bar graph.

    """
    
    # Load the Titanic dataset from the URL
    url="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
    titanic=pd.read_csv(url)
    
    titanic['survived'] = titanic['survived'].astype(str)
    
    # Create a bar plot of sex against survived
    sns.countplot(x='sex', hue='survived', data=titanic )
    
    # Add labels and title
    plt.title('Survival by Sex')
    plt.xlabel('Sex')
    plt.ylabel('count')
    plt.legend(title='survived', loc='upper right')
    
    # Show the plot
    plt.show()
    
if __name__=="__main__":
    main()