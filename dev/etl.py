from extraction import extraction_functional
from transformation import transform
from load import load_functional


def etl_process():
    # Extraction
    data = extraction_functional.extract_data()

    # Transformation
    transformed_data = transform.transform_data(data)

    # Load
    load_functional.load_data(transformed_data)
    print("ETL process completed successfully.")
    return


def main():
    etl_process()


if __name__ == "__main__":
    main()
