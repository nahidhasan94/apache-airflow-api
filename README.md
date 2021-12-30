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
### 1) Get a Simplified Representation of DAG.

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
  
