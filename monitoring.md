# Monitoring and Observability

## 🔍 CloudWatch Logs
Each Lambda function logs to its own CloudWatch log group:
- `/aws/lambda/PreprocessData`
- `/aws/lambda/TrainModel`
- `/aws/lambda/EvaluateModel`
- `/aws/lambda/DeployModel`

Logs are automatically searchable and filterable by:
- `ERROR`, `WARN`, `INFO` levels
- Step Function execution ID

## ⚡ X-Ray Integration
Enable tracing by setting `tracingConfig: ENABLED` in Lambda.
This provides:
- End-to-end execution tracing
- Latency insights across states
- Failure root cause visualization

## 🔔 Alerting
Recommended CloudWatch Alarms:
- Pipeline fails to complete (State = `FAILED`)
- Any function throws unhandled error
- Average execution time exceeds SLA threshold

Alert destinations:
- SNS topic → Email/Slack notifications
- Lambda hook → auto rollback or flag to QA team

