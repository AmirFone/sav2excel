#!/usr/bin/env python3

import argparse
import pyreadstat
import pandas as pd
import os

def convert_sav(input_path, output_path, output_format):
    """
    Convert a .sav file to either Excel (.xlsx) or CSV format.
    
    :param input_path: Path to the .sav file.
    :param output_path: Desired path for the output file (.xlsx or .csv).
    :param output_format: "xlsx" or "csv"
    """
    # Read the .sav file into a pandas DataFrame
    df, meta = pyreadstat.read_sav(input_path)
    
    # Convert the DataFrame to the desired format
    output_format = output_format.lower()
    if output_format == "csv":
        df.to_csv(output_path, index=False)
        print(f"Conversion complete! Data saved to '{output_path}' as CSV.")
    elif output_format == "xlsx":
        df.to_excel(output_path, index=False)
        print(f"Conversion complete! Data saved to '{output_path}' as Excel.")
    else:
        raise ValueError("Invalid output format. Please use 'csv' or 'xlsx'.")

def main():
    parser = argparse.ArgumentParser(
        description="Convert an SPSS .sav file to either CSV or Excel (.xlsx)."
    )
    parser.add_argument(
        "input_file",
        help="Path to the input .sav file."
    )
    parser.add_argument(
        "output_file",
        help="Path to the output file (.csv or .xlsx)."
    )
    parser.add_argument(
        "output_format",
        help="Specify 'csv' or 'xlsx' as output format."
    )
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.isfile(args.input_file):
        parser.error(f"The file {args.input_file} does not exist.")
    
    convert_sav(args.input_file, args.output_file, args.output_format)

if __name__ == "__main__":
    main()
