import pandas as pd

def dataframe_operations():
    """
    Demonstrate key DataFrame operations.
    This function creates a pandas DataFrame using a predefined dictionary
    containing information about names, ages, and cities. It then performs
    and prints various DataFrame operations.
    Returns:
        None
    """
    # Create a DataFrame from a Dictionary
    data = {
        "Name": ["Anurag", "Neha", "Ilya"],
        "Age": [39, 28, 31],
        "City": ["Munich", "Berlin", "Stockholm"]
    }

    df = pd.DataFrame(data)

    # Display the first 5 rows
    print("First 5 rows:")
    print(df.head())

    # Display the structure of the data
    print("\nDataFrame info:")
    print(df.info())

    # Display summary statistics
    print("\nSummary statistics:")
    print(df.describe())

    # Access a specific column
    print("\nName column:")
    print(df["Name"])

if __name__ == '__main__':
    dataframe_operations()
