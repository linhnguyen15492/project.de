from pymongo import MongoClient
from datetime import datetime
import pendulum
import urllib.parse

username = "linhnnh"
password = "123456"
host = "localhost"  # Or your MongoDB server's IP address/hostname
port = 27017  # Default MongoDB port
database_name = (
    "airflow"  # Database to authenticate against (optional, defaults to 'admin')
)

# Encode password to handle special characters
encoded_password = urllib.parse.quote_plus(password)

# Construct the connection URI
CONNECTION_STRING = (
    f"mongodb://{username}:{encoded_password}@{host}:{port}/{database_name}"
)

client = MongoClient(CONNECTION_STRING)


def logging(state: str) -> None:
    # Connect to a local MongoDB instance
    try:
        client = MongoClient(CONNECTION_STRING)
        collection = client.get_database("airflow").get_collection("logs")
        if collection is None:
            client.get_database("airflow").create_collection("logs")
        # Example operation: Insert a document
        collection.insert_one(
            {
                state: state,
                "date": datetime.now(tz=pendulum.timezone("Asia/Jakarta")),
            }
        )
        print("Document inserted successfully")

    except Exception as e:
        raise Exception("The following error occurred: ", e)


# This function logs the current date and state to a MongoDB collection named "logs" in the "airflow" database
# Ensure that the MongoDB connection ID "de_mongo_conn" is correctly configured in Air
logging("success")
