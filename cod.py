import pandas as pd
import json
from datetime import datetime

def convert_to_serializable(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

def extract_schema_from_excel(excel_file):
    # Read the Excel file
    xls = pd.ExcelFile(excel_file)
    schema = {}

    # Iterate over each sheet
    for sheet_name in xls.sheet_names:
        sheet_data = xls.parse(sheet_name)
        # Extract table name
        table_name = sheet_name
        # Extract column names and data types from the first two rows
        column_names = sheet_data.iloc[0].tolist()
        data_types = sheet_data.iloc[1].tolist()

        # Create a dictionary to hold the schema of the current sheet
        sheet_schema = {
            "table_name": table_name,
            "columns": {}
        }
        for col_name, data_type in zip(column_names, data_types):
            sheet_schema["columns"][col_name] = data_type

        # Add the schema of the current sheet to the overall schema
        schema[table_name] = sheet_schema

    return schema

def save_schema_as_json(schema, json_file):
    with open(json_file, 'w') as f:
        json.dump(schema, f, indent=4, default=convert_to_serializable)

# Example usage:
excel_file_path = "your_excel_file.xlsx"
schema = extract_schema_from_excel(excel_file_path)
json_file_path = "schema.json"
save_schema_as_json(schema, json_file_path)
