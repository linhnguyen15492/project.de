import json

import pendulum

from airflow.sdk import dag, task
from airflow.providers.mongo.hooks.mongo import MongoHook
from datetime import datetime


@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Jakarta"),
    catchup=False,
    tags=["example"],
)
def tutorial_taskflow_api():
    """
    ### TaskFlow API Tutorial Documentation
    This is a simple data pipeline example which demonstrates the use of
    the TaskFlow API using three simple tasks for Extract, Transform, and Load.
    Documentation that goes along with the Airflow TaskFlow API tutorial is
    located
    [here](https://airflow.apache.org/docs/apache-airflow/stable/tutorial_taskflow_api.html)
    """

    @task()
    def extract():
        """
        #### Extract task
        A simple Extract task to get data ready for the rest of the data
        pipeline. In this case, getting data is simulated by reading from a
        hardcoded JSON string.
        """
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'

        order_data_dict = json.loads(data_string)
        return order_data_dict

    @task(multiple_outputs=True)
    def transform(order_data_dict) -> dict:
        """
        #### Transform task
        A simple Transform task which takes in the collection of order data and
        computes the total order value.
        """
        total_order_value = 0

        for value in order_data_dict.values():
            total_order_value += value

        return {"total_order_value": total_order_value}

    @task()
    def load(total_order_value):
        """
        #### Load task
        A simple Load task which takes in the result of the Transform task and
        instead of saving it to end user review, just prints it out.
        """

        print(f"Total order value is: {total_order_value:.2f}")

    order_data = extract()
    order_summary = transform(order_data)
    load(order_summary["total_order_value"])  # type: ignore

    logging("TaskFlow API completed successfully")


def logging(state: str) -> None:
    try:
        mongo_hook = MongoHook(mongo_conn_id="mongoid")
        conn = mongo_hook.get_conn()
        collection = conn.get_database("airflow").get_collection("logs")
        if collection is None:
            conn.get_database("airflow").create_collection("logs")
        # Example operation: Insert a document
        collection.insert_one(
            {"state": state, "date": datetime.now(tz=pendulum.timezone("Asia/Jakarta"))}
        )
        print("Document inserted successfully")

    except Exception as e:
        raise Exception("The following error occurred: ", e)


tutorial_taskflow_api()
