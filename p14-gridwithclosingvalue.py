""" 

    @Author: Likhitha S
    @Date: 21-10-2024 13:40
    @Last Modified by: Likhitha S
    @Last Modified time: 21-10-2024 13:40
    @Title:  Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with 
    rendering with a larger grid (major grid) and a smaller grid (minor grid).Turn on the grid but turn off ticks.  
           
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    """

        Description: 
            This function is used to ploat a graph with gride lines with closing values.
        Parameters: 
           data is the dictionary that contains the data which helps used to plot lines
        return:
            It displays the graph.

    """
    
    dates = pd.date_range(start="2016-10-03", end="2016-10-07")
    closing_values = [746.62, 748.57, 753.47, 755.08, 758.87]  # Sample closing values

    # Create a DataFrame
    data = pd.DataFrame({
        'Date': dates,
        'Closing Value': closing_values
    })

    # Plotting the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Closing Value'], marker='o', linestyle='-', color='b')

    # Customizing the grid
    plt.grid(which='both', linestyle='--', linewidth=0.7)
    plt.minorticks_on()
    plt.grid(which='minor', linestyle=':', linewidth=0.5)

    # Turning off ticks
    plt.xticks([])
    plt.yticks([])

    # Adding labels and title
    plt.title('Closing Value of Alphabet Inc. (GOOGL) from Oct 3, 2016 to Oct 7, 2016')
    plt.ylabel('Closing Value (USD)')
    plt.xlabel('Date')

    # Show plot
    plt.show()
    
if __name__=="__main__":
    main()
    