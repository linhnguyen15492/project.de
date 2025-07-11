import pendulum

from airflow.sdk import dag, task
from datetime import datetime
import urllib.parse
from pymongo import MongoClient
from airflow.providers.mongo.hooks.mongo import MongoHook


username = "linhnnh"
password = "123456"
host = "localhost"  # Or your MongoDB server IP/hostname
port = 27017  # Default MongoDB port
database_name = "airflow"  # The database to connect to


encoded_username = urllib.parse.quote_plus(username)
encoded_password = urllib.parse.quote_plus(password)

CONNECTION_STRING = (
    f"mongodb://{encoded_username}:{encoded_password}@{host}:{port}/{database_name}"
)


@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Jakarta"),
    catchup=False,
    tags=["example"],
)
def logging():
    @task
    def log_to_mongo(state: str) -> None:
        try:
            # client = MongoClient(CONNECTION_STRING)
            client = MongoClient(
                "localhost",
                27017,
                connect=False,
                serverSelectionTimeoutMS=3000,
                ssl=True,
            )

            client.admin.command("ping")
            print("Connected successfully")

            collection = client.get_database("airflow").get_collection("logs")
            if collection is None:
                client.get_database("airflow").create_collection("logs")
            else:
                print("Collection already exists, inserting document")
                collection.insert_one(
                    {
                        state: state,
                        "date": datetime.now(tz=pendulum.timezone("Asia/Jakarta")),
                    }
                )
                print("Document inserted successfully")

        except Exception as e:
            raise Exception("The following error occurred: ", e)

    print("etl successfully completed")
    log_to_mongo("success")


logging_dag = logging()
# This will register the DAG with Airflow
# You can now use this DAG in your Airflow instance
# Make sure to place this file in the appropriate DAGs folder for Airflow to recognize it
# End of the logging DAG definition
# This DAG will log the current date to a MongoDB collection named "logs" in the "airflow" database
# Ensure that the MongoDB connection ID "de_mongo_conn" is correctly configured in Airflow
# and that the MongoDB server is accessible from the Airflow environment.
# The DAG is set to run manually (no schedule) and will not catch up on missed runs
# The start date is set to January 1, 2021, and the timezone is set to UTC
# The MongoDB connection uses SSL and has a connection timeout of 3000 milliseconds
