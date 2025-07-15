import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
    print(df1.head().sort_values('Difference', ascending=False))    

    # Create a scatter plot
    plt.scatter(df1['Wage'], df1['Value'])
    plt.xlabel('Wage')
    plt.ylabel('Value')
    plt.title('Wage vs Value')
    plt.show()

if __name__ == "__main__":
    main()
