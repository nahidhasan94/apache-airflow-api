# apache-airflow-api

(Here DAG Id = example_trigger_target_dag)
**DAG Run API 
1) Trigger a new DAG run with Config.

***request:
curl -X 'POST' \
  'http://localhost:8080/api/v1/dags/example_trigger_target_dag/dagRuns' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "conf": {"message":"nahid"}
}'

***response:
{
  "conf": {
    "message": "nahid"
  },
  "dag_id": "example_trigger_target_dag",
  "dag_run_id": "manual__2021-12-30T07:54:07.429904+00:00",
  "end_date": null,
  "execution_date": "2021-12-30T07:54:07.429904+00:00",
  "external_trigger": true,
  "logical_date": "2021-12-30T07:54:07.429904+00:00",
  "start_date": null,
  "state": "queued"
}

2) 
