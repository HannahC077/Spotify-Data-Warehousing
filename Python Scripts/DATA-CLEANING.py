import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk
import numpy as np 
from tqdm import tqdm
import pandas as pd
from scipy.stats import zscore
from datetime import datetime


def extract_date_information(df, column_name):
    """
    Extract day, month, and day of the week from a column with date-like strings.

    Parameters:
    - file_path: The csv containing the data.
    - column_name (str): The name of the column containing date-like strings.

    Returns:
    - pd.DataFrame: A DataFrame with added columns for day, month, and day of the week.
    """
    print(df.columns)

    # Ensure the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError("Column '{column_name}' not found in the DataFrame.")

    # Create new columns for day, month, and day of the week
    df['day'] = 1  # Substitute 1 for day
    df['month'] = 1  # Substitute 1 for month
    df['day_of_week'] = 1  # Substitute 1 for day of the week

    # Update the columns based on the actual date information
    for index, date_str in enumerate(df[column_name]):
        try:
            date_obj = pd.to_datetime(date_str)
            df.at[index, 'day'] = date_obj.day
            df.at[index, 'month'] = date_obj.month
            df.at[index, 'day_of_week'] = date_obj.dayofweek  # Adding 1 to make Monday=1, Sunday=7 but for now Mon = 0 && Sun = 6
        except ValueError:
            # Handle the case where the date string is not in a recognized format
            print("Skipping invalid date: {date_str} at index {index}")

    return df

def calculate_z_score(file_path, column_name):
    """
    Calculate the z-score for a specific column in a DataFrame.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame containing the data.
    - column_name (str): The name of the column for which to calculate the z-score.

    Returns:
    - pd.Series: A Series containing the z-scores for the specified column.
    """

    dataframe = pd.read_excel(file_path)
    # Check if the specified column exists in the DataFrame
    if column_name not in dataframe.columns:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

    # Calculate z-score using scipy.stats.zscore
    z_score_series = zscore(dataframe[column_name])
    print("Z Score: ", z_score_series)

    return pd.Series(z_score_series, name=f'{column_name}_z_score')


def choose_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select EXCEL file", filetypes=[("EXCEL files", "*.xlsx")])
    return file_path

def visualize_right_skewed_dataset(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_excel(file_path)

    # Check the first few rows of the DataFrame
    print("Sample of the dataset:")
    print(df.head())

    # Visualize the right-skewed dataset
    plt.figure(figsize=(10, 6))
    plt.hist(df['streams'], bins=30, color='skyblue', edgecolor='black', density=True)
    plt.title('Histogram of the "streams" Column')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.boxplot(df['streams'], vert=False)
    plt.title('Box Plot of the "streams" Column')
    plt.xlabel('Values')
    plt.yticks([])
    plt.grid(True)
    plt.show()


def normalize_and_export_dataset(df):
    df['streams_log'] = np.log1p(df['streams'])  # log1p(x) computes log(1 + x)
    
    # Ask the user to select the directory and specify the file name
    root = tk.Tk()
    root.withdraw()
    new_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                  filetypes=[("Excel files", "*.xlsx")],
                                                  title="Save the Normalized Dataset As")
    
    if new_file_path:
        # Display a loading bar while exporting
        tqdm.pandas()
        df.progress_apply(lambda _: tqdm.write('.', end=''), axis=1)
        
        # Export the DataFrame to the new EXCEL file
        df.to_excel(new_file_path, index=False)
        
        print("\nNormalized dataset exported to: {new_file_path}")
    else:
        print("Export canceled.")

if __name__ == "__main__":
    # Replace 'your_dataset.xlsx' with the actual EXCEL file path
    df = pd.read_excel(choose_file())
    #df = extract_date_information(df, "release_date")
    normalize_and_export_dataset(df)


    # Z Scores:
    # z_scores = calculate_z_score(file_path, "streams")
    # print("Z Scores:", z_scores)


    # visualize_right_skewed_dataset(file_path)

    # Normalize the dataset and export to a new CSV file
    # normalize_and_export_dataset(file_path)

    #visualize_right_skewed_dataset(file_path)
    
    # Normalize the dataset and export to a new CSV file
    #normalize_and_export_dataset(file_path)