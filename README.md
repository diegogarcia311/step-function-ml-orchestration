# Step Function ML Orchestration

This project demonstrates a modular, scalable machine learning retraining pipeline using AWS Step Functions, Lambda, and CloudWatch. Designed for SLA-bound, audit-compliant retraining workflows in regulated or mission-critical environments.

---

## 🔍 Use Case

Automated retraining of deployed ML models (e.g., underwriting risk models or fraud classifiers) triggered by:
- Data freshness
- SLA-driven schedules
- Performance degradation (via drift detection)

---

## 🏗️ Key Components

- **Step Functions**: Manages stateful orchestration of retraining steps with retry logic
- **Lambda Functions**: Trigger data preprocessing, model retraining, evaluation, and deployment
- **CloudWatch**: Centralized logging and performance metrics
- **X-Ray**: Traces failures and performance bottlenecks

---

## 🧱 Folder & File Overview

- `step_functions_definition.json`: Full AWS Step Functions definition with states, retries, and error handling
- `pipeline_orchestration.py`: Logic for controlling orchestration sequence
- `model_retraining_trigger.py`: Trigger Lambda to initiate the pipeline (via time, data drift, or event)
- `monitoring.md`: CloudWatch/X-Ray setup for visibility and alerting

---

## 📈 Monitoring

- CloudWatch Logs grouped by function
- X-Ray enabled for trace-level analysis
- Custom CloudWatch Alarms (e.g., job failure, SLA miss)

---

## 🧪 Future Enhancements

- Add SageMaker integration for large-scale training
- Connect to S3 for automatic data ingestion
- Add Slack/Email notifications on retrain completion/failure
- Version registry integration (e.g., MLflow, SageMaker Model Registry)

---
