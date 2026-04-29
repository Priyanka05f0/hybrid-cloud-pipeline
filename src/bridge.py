import json
import time
import boto3
from google.cloud import pubsub_v1

# LocalStack SQS
sqs = boto3.client(
    "sqs",
    endpoint_url="http://localhost:4566",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

queue_url = "http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/hybrid-queue"

# GCP Pub/Sub
project_id = "project-dd166e03-7284-484d-a0c"
topic_id = "bridge-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

print("Bridge app started...")

while True:
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=5
    )

    messages = response.get("Messages", [])

    for msg in messages:
        body = msg["Body"]

        publisher.publish(topic_path, body.encode("utf-8"))
        print("Sent to Pub/Sub:", body)

        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=msg["ReceiptHandle"]
        )

    time.sleep(2)