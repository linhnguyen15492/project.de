# ghi chú

- host khi thiet lap airflow connection la: host.docker.internal

```bash
docker run --name airflow_ct -p 8080:8080 -v ./airflow:/opt/airflow d1a74224f2a6 standalone
```

cd /mnt/d
To access your host (Windows) drives from within WSL (Windows Subsystem for Linux), you can use the /mnt/ directory. Windows drives are automatically mounted there, with the drive letter as the directory name. For example, your C: drive would be accessible at /mnt/c/, and your D: drive at /mnt/d/. You can also access the WSL file system from Windows File Explorer using the UNC path `\\wsl$`

To set the Airflow home directory to the current directory, you can use the command export AIRFLOW_HOME="$(pwd)". This command will set the AIRFLOW_HOME environment variable to the absolute path of your current working directory. This is the recommended way to set the Airflow home directory, especially when you want to keep your Airflow configuration and data in the same directory as your project.

```bash
export AIRFLOW_HOME=/home/project/airflow

cp dummy_dag.py $AIRFLOW_HOME/dags

airflow dags list

airflow dags list | grep dummy_dag

airflow dags list | grep dummy_dag

airflow tasks list dummy_dag
```

```bash
export AIRFLOW_HOME=/home/project/airflow
echo $AIRFLOW_HOME

cp my_first_dag.py $AIRFLOW_HOME/dags

airflow dags list

airflow dags list|grep "my-first-python-etl-dag"

airflow tasks list my-first-python-etl-dag
```

```bash
cp ETL_Server_Access_Log_Processing.py $AIRFLOW_HOME/dags
airflow dags list | grep etl-server-logs-dag
airflow dags list-import-errors

```

## setup airflow local

- cd airflow
- export AIRFLOW_HOME="$(pwd)"
- echo $AIRFLOW_HOME
- pip install graphviz

airflow dag-processor
airflow dags list

airflow db reset

pip install flask-appbuilder
