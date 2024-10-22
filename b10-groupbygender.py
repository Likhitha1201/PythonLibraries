""" 
    @Author: Likhitha S
    @Date: 22-10-2024 12:40
    @Last Modified by: Likhitha S
    @Last Modified time: 22-10-2024 12:40
    @Title: Write a Python program to create bar plot of scores by group and gender. Use multiple X values on the same chart for men and women. 

"""
import matplotlib.pyplot as plt
import numpy as np

def main():
    """

        Description: 
            This function is used to plot a bar graph .
        Parameters: 
            prg_lang, popularity are the list of points that as to be displayed on graph.
        return:
            It displays the bar graph.

    """
    
    men=(22, 30, 35, 35, 26)
    women=(25, 32, 30, 35, 29)
    group=['g1','g2','g3','g4','g5']
    
    # setting position s to bar
    x=np.arange(len(group))
    width=0.39
    fig, new=plt.subplots()
    # here we are using multiple of x with the men and women
    bar1= new.bar(x - width/2, women, width, color='g', label='womens')
    bar2= new.bar(x + width/2, men , width, color='y', label="mens")
    
    new.set_title("Scores by group and gender")
    new.set_xlabel("groups")
    new.set_ylabel("scores")
    # where xticks and xticklabels help to label the horizonal line / graph
    new.set_xticks(x)
    new.legend()
    new.set_xticklabels(group)
    
    plt.tight_layout()
    
    plt.show()
    
if __name__=="__main__":
    main()