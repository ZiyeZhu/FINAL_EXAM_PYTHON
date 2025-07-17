# load_data.py
import pandas as pd

def load_excel_data(file_path: str, sheet_name: str) -> pd.DataFrame:
    """
    Loads an Excel file and returns a DataFrame from the specified sheet.

    Parameters:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet to load.

    Returns:
        pd.DataFrame: The loaded data.
    """
    excel_file = pd.ExcelFile(file_path)
    print("Available sheets:", excel_file.sheet_names)
    df = excel_file.parse(sheet_name)
    return df