import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("stepfunctions")

    response = client.start_execution(
        stateMachineArn="arn:aws:states:REGION:ACCOUNT_ID:stateMachine:MLRetrainingPipeline",
        name=f"retrain-{context.aws_request_id}",
        input=json.dumps({"trigger_type": "scheduled"})
    )

    return {
        "statusCode": 200,
        "body": json.dumps("Retraining pipeline initiated.")
    }

