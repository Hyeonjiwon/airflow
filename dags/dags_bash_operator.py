from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

from airflow.operators.empty import EmptyOperator

# DAG 정의, 필수
with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 3, 1, tz="Asia/Seoul"),  
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"],
    # params={"example_key": "example_value"},
) as dag:
    # [START howto_operator_bash]  
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo who am i",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )
    
    bash_t1 >> bash_t2