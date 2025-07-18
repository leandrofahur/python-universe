import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show
from bokeh.models import HoverTool
import seaborn as sns


sns.set()


# Convert 'K' and 'M'
def convert_wage_string(wage_str):
    if 'K' in wage_str:
        return float(wage_str.replace('K', '')) * 1000
    elif 'M' in wage_str:
        return float(wage_str.replace('M', '')) * 1000000
    elif 'B' in wage_str:
        return float(wage_str.replace('B', '')) * 1000000000
    else:
        return float(wage_str)


def main():
    # Import the data:
    df = pd.read_csv("./datasets/data.csv")
    # print(df.shape)        
    # print(df.describe())
    df1 = pd.DataFrame(df,columns=["Name","Wage","Value"])
    # print(df1.head())
        
    # Remove '$' and ','
    df1['Wage'] = df1['Wage'].str.replace('€', '').str.replace(',', '')
    df1['Wage'] = df1['Wage'].apply(convert_wage_string)
    
    df1['Value'] = df1['Value'].str.replace('€', '').str.replace(',', '')
    df1['Value'] = df1['Value'].apply(convert_wage_string)
    df1['Difference'] = df1['Value'] - df1['Wage']
    # print(df1.head().sort_values('Difference', ascending=False))    

    # Create a scatter plot
    # plt.scatter(df1['Wage'], df1['Value'])
    # plt.xlabel('Wage')
    # plt.ylabel('Value')
    # plt.title('Wage vs Value')
    # plt.show()

    # sns.scatterplot(x='Wage', y='Value', data=df1)
    # plt.show()

    TOOLTIPS = [
        ("x", "@Wage"),
        ("y", "@Value"),
        ("Name", "@Name"),
        ("Difference", "@Difference")
    ]
    
    p = figure(width=800, height=800, title="Wage vs Value", x_axis_label='Wage', y_axis_label='Value', tooltips=TOOLTIPS)    
    p.scatter(x='Wage', y='Value', size=10, source=df1)
    show(p)


if __name__ == "__main__":
    main()
