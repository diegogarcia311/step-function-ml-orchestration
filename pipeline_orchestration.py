import boto3

def start_pipeline(execution_name="ml-retraining-exec"):
    client = boto3.client("stepfunctions")

    response = client.start_execution(
        stateMachineArn="arn:aws:states:REGION:ACCOUNT_ID:stateMachine:MLRetrainingPipeline",
        name=execution_name,
        input='{"trigger": "scheduled_retrain"}'
    )

    print("Pipeline execution started:", response["executionArn"])

if __name__ == "__main__":
    start_pipeline()
