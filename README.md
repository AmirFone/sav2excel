
# sav2excel

A minimal Python utility that converts SPSS (.sav) files into Excel-compatible (.xlsx) files using `pyreadstat` and `pandas`.

## Usage

1. Install dependencies:
   ```bash
   pip install pyreadstat pandas openpyxl
   ```

2. Run the script:
   ```bash
   python sav_to_excel.py /path/to/input_file.sav /path/to/output_file.xlsx
   ```
3. Run the script with .csv output:
   ```bash
   python sav_converter.py /path/to/input_file.sav /path/to/output_file.csv csv

   ```

Replace `/path/to/input_file.sav` and `/path/to/output_file.xlsx` with the appropriate file paths.
