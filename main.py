from extraction import extraction_functional


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


def main():
    csv_file_name = "data/h9gi-nx95.csv"
    db_name = "data/movies.sqlite"
    df_csv = extraction_functional.source_data_from_csv(csv_file_name)
    print(df_csv.head(5))
    df_table = extraction_functional.source_data_from_table(db_name, "movies")
    print(df_table.head(5))


def test_packages():
    from src.extraction import extractor

    extractor.test()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

