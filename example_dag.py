from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator


@task(task_id="run_this")
def run_this_func(dag_run=None):
    """
    Print the payload "message" passed to the DagRun conf attribute.
    :param dag_run: The DagRun object
    :type dag_run: DagRun
    """
    print(f"Remotely received value of {dag_run.conf.get('message')} for key=message")


with DAG(
    dag_id="example_trigger_target_dag",
    start_date=datetime(2021, 1, 1),
    catchup=False,
    schedule_interval=None,
    tags=['example'],
) as dag:
    run_this = run_this_func()

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command='echo "Here is the message: $message"',
        env={'message': '{{ dag_run.conf.get("message") }}'},
    )
