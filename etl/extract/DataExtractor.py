from abc import ABC, abstractmethod


class DataExtractor(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def extract_data(self, source_type, source_config):
        # This method will be implemented by subclasses
        raise NotImplementedError


class CSVExtractor(DataExtractor):
    def __init__(self, config):
        super().__init__(config)

    def extract_data(self, source_type, source_config):
        if source_type == "csv":
            print(f"Extracting data from CSV: {source_config['path']}")
            # Here you would add the actual CSV extraction logic
            # For demonstration, let's return some dummy data
            return [
                {"col1": "csv_val1", "col2": "csv_val2"},
                {"col1": "csv_val3", "col2": "csv_val4"},
            ]
        else:
            raise ValueError(f"Unsupported source type for CSVExtractor: {source_type}")


class DatabaseExtractor(DataExtractor):
    def __init__(self, config):
        super().__init__(config)

    def extract_data(self, source_type, source_config):
        if source_type == "database":
            print(
                f"Extracting data from Database: {source_config['connection_string']}"
            )
            # Here you would add the actual database extraction logic
            # For demonstration, let's return some dummy data
            return [
                {"colA": "db_valA", "colB": "db_valB"},
                {"colA": "db_valC", "colB": "db_valD"},
            ]
        else:
            raise ValueError(
                f"Unsupported source type for DatabaseExtractor: {source_type}"
            )


class APIExtractor(DataExtractor):
    def __init__(self, config):
        super().__init__(config)

    def extract_data(self, source_type, source_config):
        if source_type == "api":
            print(f"Extracting data from API: {source_config['endpoint']}")
            # Here you would add the actual API extraction logic
            # For demonstration, let's return some dummy data
            return [
                {"field1": "api_data1", "field2": "api_data2"},
                {"field1": "api_data3", "field2": "api_data4"},
            ]
        else:
            raise ValueError(f"Unsupported source type for APIExtractor: {source_type}")


class ExcelExtractor(DataExtractor):
    def __init__(self, config):
        super().__init__(config)

    def extract_data(self, source_type, source_config):
        if source_type == "excel":
            print(f"Extracting data from Excel: {source_config['path']}")
            # Here you would add the actual Excel extraction logic
