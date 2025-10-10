import os
from extraction import extractor
import os
import openpyxl
import pandas as pd
import dask.dataframe as dd

print("import thành công")
print(os.getcwd())
script_directory = os.path.dirname(os.path.realpath(__file__))
print(script_directory)


folder_path = "D:\\_workspace\\_billing\\_FEE sources"
for filename in os.listdir(folder_path):
    filepath = os.path.join(folder_path, filename)
    print(filepath)
    if "MSN" in filename:
        try:
            df = pd.read_excel(filepath)
            dask_df = dd.from_pandas(df, npartitions=4)
            print(dask_df.head())
        except Exception as e:
            print(e)
