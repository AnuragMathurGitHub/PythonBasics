import pandas as pd

def create_dataframe():
    """
    Create a DataFrame from a dictionary and print it.
    This function creates a pandas DataFrame using a predefined dictionary
    containing information about names, ages, and cities. It then prints
    the DataFrame to the console.
    Returns:
        None
    """
    # Create a DataFrame from a Dictionary
    data = {
        "Name": ["Anurag", "Neha", "Ilya"],
        "Age": [25, 28, 31],
        "City": ["Munich", "Berlin", "Stockholm"]
    }

    df = pd.DataFrame(data)
    print(df)

if __name__ == '__main__':
    create_dataframe()
