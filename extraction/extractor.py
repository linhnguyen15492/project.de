import pandas as pd
import os


def extract_from_excel(path: str, sheetname: str, mappings: dict) -> pd.DataFrame:
    """
    Docstring: extract data from excel file, add new column to tracking source, rename column to match with db schema

    Args:
        parameter1 (str): Path of excel file
        parameter2 (str): sheetname to extract
        parameter3 (dict): extract columns and then rename
        *args: Description of arbitrary positional arguments.
        **kwargs: Description of arbitrary keyword arguments.

    Returns:
        type: dataframe
    """
    # read excel file
    try:
        df = pd.read_excel(path, sheet_name=sheetname)

        # add column to note datasource
        filename = str(path.split("\\")[-1].strip())
        df["reference_source"] = filename

        # add new column to mappings object
        mappings["reference_source"] = "reference_source"

        # rename columns to matching with database
        df.rename(columns=mappings, inplace=True)

        return df[[col for col in mappings.values()]]

    except Exception as e:
        print(f"Fail to read {path} with sheet {sheetname}")

    return pd.DataFrame()


def test():
    print("message from extractor module")


def main():
    folder_name = ".data"
    filename = "20250831_FEE_030000.xlsx"
    path = os.path.join(os.getcwd(), folder_name, filename)
    print(path)
    # for file in os.listdir(path):
    #     print(file)

    packed_mapping = {
        "Ngày tạo SO": "so_date",
        "Mã SO Eton": "so_number",
        "Mã SO client": "so_number_client",
        "BizType": "biztype",
    }

    sheetname = "Packed"

    df = extract_from_excel(path, sheetname=sheetname, mappings=packed_mapping)
    print(df.head())


if __name__ == "__main__":
    main()
