import pendulum

from airflow.sdk import dag, task
from airflow.providers.mongo.hooks.mongo import MongoHook
from datetime import datetime


@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def logging():
    @task
    def log_to_mongo():
        try:
            mongo_hook = MongoHook(mongo_conn_id="de_mongo_conn")
            conn = mongo_hook.get_conn()
            collection = conn.get_database("airflow").get_collection("logs")
            if collection is None:
                conn.get_database("airflow").create_collection("logs")
            # Example operation: Insert a document
            collection.insert_one({"date": datetime.now()})
            print("Document inserted successfully")

        except Exception as e:
            raise Exception("The following error occurred: ", e)

    log_to_mongo()


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
