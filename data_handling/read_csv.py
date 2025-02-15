import pandas as pd
import os

def read_csv_file(file_path):
    """
    Read data from a CSV file and print it.
    This function reads a CSV file using pandas and prints the DataFrame to the console.
    Parameters:
        file_path (str): The path to the CSV file.
    Returns:
        None
    """
    df = pd.read_csv(file_path)
    #print(df)
    print(df.head())  # First 5 rows
    print(df.info())  # Structure of data
    print(df.describe())  # Summary statistics
    print(df["Name"])  # Access a column

if __name__ == '__main__':
    # Get the absolute path of the CSV file
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, 'data', 'people.csv')
    read_csv_file(csv_path)
