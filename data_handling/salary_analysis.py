import pandas as pd
import os

def analyze_salaries(file_path):
    """
    Analyze employee salaries from a CSV file.
    This function reads a CSV file containing employee salary data, performs
    various analyses, and prints the results to the console.
    Parameters:
        file_path (str): The path to the CSV file.
    Returns:
        None
    """
    df = pd.read_csv(file_path)

    # Display the first 5 rows
    print("First 5 rows:")
    print(df.head())

    # Display the structure of the data
    print("\nDataFrame info:")
    print(df.info())

    # Display summary statistics
    print("\nSummary statistics:")
    print(df.describe())

    # Calculate the average salary
    average_salary = df['Salary'].mean()
    print(f"\nAverage Salary: {average_salary}")

    # Calculate the maximum salary
    max_salary = df['Salary'].max()
    print(f"Maximum Salary: {max_salary}")

    # Calculate the minimum salary
    min_salary = df['Salary'].min()
    print(f"Minimum Salary: {min_salary}")

    # Group by department and calculate average salary
    avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
    print("\nAverage Salary by Department:")
    print(avg_salary_by_dept)

if __name__ == '__main__':
    # Get the absolute path of the CSV file
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, 'data', 'salaries.csv')
    analyze_salaries(csv_path)
