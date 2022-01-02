# apache-airflow-api

(Here DAG Id = example_trigger_target_dag)
## DAG Run API
### 1) Trigger a new DAG run with Config.

**request:**
```
curl -X 'POST' \
  'http://localhost:8080/api/v1/dags/example_trigger_target_dag/dagRuns' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "dag_run_id": "mydagrunid",
  "execution_date": "2019-08-24T14:15:22Z",
  "conf": "message":"nahid"}
}'
```
**response:**
```
{
  "conf": {
    "message": "nahid"
  },
  "dag_id": "example_trigger_target_dag",
  "dag_run_id": "mydagrunid",
  "end_date": null,
  "execution_date": "2021-12-30T07:54:07.429904+00:00",
  "external_trigger": true,
  "logical_date": "2021-12-30T07:54:07.429904+00:00",
  "start_date": null,
  "state": "queued"
}
```
### 2) Get List of Dag Run

**request:**
```
curl -X 'GET' \
  'http://localhost:8080/api/v1/dags/example_trigger_target_dag/dagRuns?limit=100' \
  -H 'accept: application/json'
```
**response:**
```
{
  "dag_runs": [
    {
      "conf": {
        "message": "i am here"
      },
      "dag_id": "example_trigger_target_dag",
      "dag_run_id": "example_trigger_target_dag",
      "end_date": "2021-12-30T07:51:31.480677+00:00",
      "execution_date": "2021-12-30T07:36:37.752000+00:00",
      "external_trigger": true,
      "logical_date": "2021-12-30T07:36:37.752000+00:00",
      "start_date": "2021-12-30T07:51:18.815929+00:00",
      "state": "success"
    },
    {
      "conf": {
        "message": "its working fine"
      },
      "dag_id": "example_trigger_target_dag",
      "dag_run_id": "manual2021-12-30T07:49:42.570662+00:00",
      "end_date": "2021-12-30T07:51:31.492989+00:00",
      "execution_date": "2021-12-30T07:49:42.570662+00:00",
      "external_trigger": true,
      "logical_date": "2021-12-30T07:49:42.570662+00:00",
      "start_date": "2021-12-30T07:51:18.815975+00:00",
      "state": "success"
    },
    {
      "conf": {
        "message": "nahid hasan"
      },
      "dag_id": "example_trigger_target_dag",
      "dag_run_id": "manual2021-12-30T07:54:07.429904+00:00",
      "end_date": "2021-12-30T07:54:14.068046+00:00",
      "execution_date": "2021-12-30T07:54:07.429904+00:00",
      "external_trigger": true,
      "logical_date": "2021-12-30T07:54:07.429904+00:00",
      "start_date": "2021-12-30T07:54:08.263644+00:00",
      "state": "success"
    },
    {
      "conf": {
        "message": "nahid"
      },
      "dag_id": "example_trigger_target_dag",
      "dag_run_id": "mydagrunid",
      "end_date": "2021-12-30T07:55:34.517443+00:00",
      "execution_date": "2021-12-30T07:55:27.528053+00:00",
      "external_trigger": true,
      "logical_date": "2021-12-30T07:55:27.528053+00:00",
      "start_date": "2021-12-30T07:55:28.231721+00:00",
      "state": "success"
    }
  ],
  "total_entries": 4
}
```

### 3) Get a Dag Run

**request:**
```
curl -X 'GET' \
  'http://localhost:8080/api/v1/dags/example_trigger_target_dag/dagRuns/mydagrunid' \
  -H 'accept: application/json'
```
**response:**
```
{
  "conf": {
    "message": "nahid"
  },
  "dag_id": "example_trigger_target_dag",
  "dag_run_id": "mydagrunid",
  "end_date": "2021-12-30T09:51:04.325511+00:00",
  "execution_date": "2021-12-30T09:50:57.714516+00:00",
  "external_trigger": true,
  "logical_date": "2021-12-30T09:50:57.714516+00:00",
  "start_date": "2021-12-30T09:50:58.337474+00:00",
  "state": "success"
}
```

## DAG API
### 1) Get List of DAG.

**request:**
```
curl -X 'GET' \
  'http://localhost:8080/api/v1/dags?limit=100&only_active=true' \
  -H 'accept: application/json'
```
**response:**
```
{
  "dags": [
    {
      "dag_id": "example_trigger_target_dag",
      "description": null,
      "file_token": "Ii9vcHQvYWlyZmxvdy9kYWdzL3BhcmFtZGFnLnB5Ig.hhWlYRe7zNQ_VEX9RUv6afx1pbs",
      "fileloc": "/opt/airflow/dags/paramdag.py",
      "is_active": true,
      "is_paused": false,
      "is_subdag": false,
      "owners": [
        "airflow"
      ],
      "root_dag_id": null,
      "schedule_interval": null,
      "tags": [
        {
          "name": "example"
        }
      ]
    },
    {
      "dag_id": "hello_world",
      "description": "Hello World DAG",
      "file_token": "Ii9vcHQvYWlyZmxvdy9kYWdzL2hlbGxvLXdvcmxkLnB5Ig.EBqbQi-3Je7WvYG0GwtuXGN5UrY",
      "fileloc": "/opt/airflow/dags/hello-world.py",
      "is_active": true,
      "is_paused": false,
      "is_subdag": false,
      "owners": [
        "airflow"
      ],
      "root_dag_id": null,
      "schedule_interval": {
        "__type": "CronExpression",
        "value": "0 12 * * *"
      },
      "tags": []
    },
    {
      "dag_id": "tutorial",
      "description": "A simple tutorial DAG",
      "file_token": "Ii9vcHQvYWlyZmxvdy9kYWdzL3Rlc3QxLnB5Ig.ZfAACfnJFXtzC7so9yhfdo1IGKU",
      "fileloc": "/opt/airflow/dags/test1.py",
      "is_active": true,
      "is_paused": true,
      "is_subdag": false,
      "owners": [
        "airflow"
      ],
      "root_dag_id": null,
      "schedule_interval": {
        "__type": "TimeDelta",
        "days": 1,
        "microseconds": 0,
        "seconds": 0
      },
      "tags": [
        {
          "name": "example"
        }
      ]
    }
  ],
  "total_entries": 3
}
```
### 2) Get a Simplified Representation of DAG.

**request:**
```
curl -X 'GET' \
  'http://localhost:8080/api/v1/dags/example_trigger_target_dag/details' \
  -H 'accept: application/json'
 ```
 **response:**
```
{
  "catchup": false,
  "concurrency": 16,
  "dag_id": "example_trigger_target_dag",
  "dag_run_timeout": null,
  "default_view": "tree",
  "description": null,
  "doc_md": null,
  "file_token": "Ii9vcHQvYWlyZmxvdy9kYWdzL3BhcmFtZGFnLnB5Ig.hhWlYRe7zNQ_VEX9RUv6afx1pbs",
  "fileloc": "/opt/airflow/dags/paramdag.py",
  "is_active": true,
  "is_paused": false,
  "is_subdag": false,
  "max_active_tasks": 16,
  "orientation": "LR",
  "owners": [
    "airflow"
  ],
  "params": {},
  "schedule_interval": null,
  "start_date": "2021-01-01T00:00:00+00:00",
  "tags": [
    {
      "name": "example"
    }
  ],
  "timezone": "Timezone('UTC')"
}
```
### 3) Get tasks of DAG.

**request:**
```
curl -X 'GET' \
  'http://localhost:8080/api/v1/dags/example_trigger_target_dag/tasks' \
  -H 'accept: application/json'
```
 **response:**
```
{
  "tasks": [
    {
      "class_ref": {
        "class_name": "BashOperator",
        "module_path": "airflow.operators.bash"
      },
      "depends_on_past": false,
      "downstream_task_ids": [],
      "end_date": null,
      "execution_timeout": null,
      "extra_links": [],
      "owner": "airflow",
      "params": {},
      "pool": "default_pool",
      "pool_slots": 1,
      "priority_weight": 1,
      "queue": "default",
      "retries": 0,
      "retry_delay": {
        "__type": "TimeDelta",
        "days": 0,
        "microseconds": 0,
        "seconds": 300
      },
      "retry_exponential_backoff": false,
      "start_date": "2021-01-01T00:00:00+00:00",
      "task_id": "bash_task",
      "template_fields": [
        "bash_command",
        "env"
      ],
      "trigger_rule": "all_success",
      "ui_color": "#f0ede4",
      "ui_fgcolor": "#000",
      "wait_for_downstream": false,
      "weight_rule": "downstream"
    },
    {
      "class_ref": {
        "class_name": "_PythonDecoratedOperator",
        "module_path": "airflow.decorators.python"
      },
      "depends_on_past": false,
      "downstream_task_ids": [],
      "end_date": null,
      "execution_timeout": null,
      "extra_links": [],
      "owner": "airflow",
      "params": {},
      "pool": "default_pool",
      "pool_slots": 1,
      "priority_weight": 1,
      "queue": "default",
      "retries": 0,
      "retry_delay": {
        "__type": "TimeDelta",
        "days": 0,
        "microseconds": 0,
        "seconds": 300
      },
      "retry_exponential_backoff": false,
      "start_date": "2021-01-01T00:00:00+00:00",
      "task_id": "run_this",
      "template_fields": [
        "op_args",
        "op_kwargs"
      ],
      "trigger_rule": "all_success",
      "ui_color": "#ffefeb",
      "ui_fgcolor": "#000",
      "wait_for_downstream": false,
      "weight_rule": "downstream"
    }
  ],
  "total_entries": 2
}
```
### 4) Get Simplified Representation of Task.

**request:**
```
curl -X 'GET' \
  'http://localhost:8080/api/v1/dags/example_trigger_target_dag/tasks/bash_task' \
  -H 'accept: application/json'
  
 ```
 **response:**
```
{
  "class_ref": {
    "class_name": "BashOperator",
    "module_path": "airflow.operators.bash"
  },
  "depends_on_past": false,
  "downstream_task_ids": [],
  "end_date": null,
  "execution_timeout": null,
  "extra_links": [],
  "owner": "airflow",
  "params": {},
  "pool": "default_pool",
  "pool_slots": 1,
  "priority_weight": 1,
  "queue": "default",
  "retries": 0,
  "retry_delay": {
    "__type": "TimeDelta",
    "days": 0,
    "microseconds": 0,
    "seconds": 300
  },
  "retry_exponential_backoff": false,
  "start_date": "2021-01-01T00:00:00+00:00",
  "task_id": "bash_task",
  "template_fields": [
    "bash_command",
    "env"
  ],
  "trigger_rule": "all_success",
  "ui_color": "#f0ede4",
  "ui_fgcolor": "#000",
  "wait_for_downstream": false,
  "weight_rule": "downstream"
}
 ```
 
 ### 5) Update A DAG (Use to Pause the dag or UnPause the dag).

**request:**
```
curl -X 'PATCH' \
  'http://localhost:8080/api/v1/dags/example_trigger_target_dag' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "is_paused": false
}'
  
```
 **response:**
```
{
  "dag_id": "example_trigger_target_dag",
  "description": null,
  "file_token": "Ii9vcHQvYWlyZmxvdy9kYWdzL3BhcmFtZGFnLnB5Ig.hhWlYRe7zNQ_VEX9RUv6afx1pbs",
  "fileloc": "/opt/airflow/dags/paramdag.py",
  "is_active": true,
  "is_paused": false,
  "is_subdag": false,
  "owners": [
    "airflow"
  ],
  "root_dag_id": null,
  "schedule_interval": null,
  "tags": [
    {
      "name": "example"
    }
  ]
}
 ```
 
