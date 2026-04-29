# Hybrid Cloud Data Pipeline with LocalStack and Google Cloud Platform

## Project Overview

This project demonstrates a hybrid cloud data pipeline by integrating LocalStack (AWS cloud simulation) with Google Cloud Platform services. It simulates a real-world multi-cloud architecture where data originates in one cloud environment and is processed in another.

The pipeline uses LocalStack services such as Amazon S3, Amazon SQS, and DynamoDB, while Google Cloud services such as Pub/Sub, Cloud Functions, and Cloud SQL are used for processing and storage.

---

## Objective

To build an automated hybrid cloud pipeline where:

1. Data is generated in LocalStack (AWS simulated environment)
2. Messages are sent through LocalStack SQS
3. A Python bridge application transfers messages to Google Pub/Sub
4. Google Cloud Function processes incoming messages
5. Processed records are stored in Google Cloud SQL

---

## Architecture

```text
LocalStack S3 / SQS
        ↓
Python Bridge Application
        ↓
Google Pub/Sub
        ↓
Google Cloud Function
        ↓
Google Cloud SQL
```

## Technologies Used

### Cloud Platforms
- Google Cloud Platform (GCP)
- LocalStack (AWS local emulator)
## AWS Simulated Services
- Amazon S3
- Amazon SQS
- DynamoDB
### Google Cloud Services
- Pub/Sub
- Cloud Functions (Gen2)
- Cloud SQL (MySQL)
### DevOps / Tools
- Docker
- Terraform
- Python 3.11
- Git Bash
- VS Code

---

## Project Structure
```
hybrid-cloud-pipeline/
├── docker-compose.yml
├── Dockerfile
├── README.md
├── .env.example
├── submission.json
├── src/
│   ├── bridge.py
│   ├── main.py
│   └── requirements.txt
└── terraform/
    ├── main.tf
    ├── providers.tf
    ├── variables.tf
    └── output.tf
```
## Setup Instructions

### Step 1: Start LocalStack
```bash
docker compose up -d
```

### Step 2: Provision Infrastructure using Terraform
```bash
cd terraform
terraform init
terraform apply -auto-approve
```
This creates:
- S3 bucket
- SQS queue
- DynamoDB table
- Pub/Sub topic

### Step 3: Run Bridge Application
```bash
cd ../src
python bridge.py
```
The bridge polls SQS messages and publishes them to Pub/Sub.

### Step 4: Deploy Cloud Function
```bash
gcloud functions deploy process_pubsub \
--runtime python311 \
--trigger-topic bridge-topic \
--entry-point process_pubsub \
--region us-central1 \
--gen2 \
--allow-unauthenticated
```

### Step 5: Cloud SQL Setup
Create:
- Cloud SQL Instance
- Database: hybriddb
- Table: records
```sql
CREATE TABLE records (
 id VARCHAR(50),
 name VARCHAR(100),
 course VARCHAR(100),
 processed_timestamp VARCHAR(100)
);
```

### Testing the Pipeline
Send test message:
```bash
aws --endpoint-url=http://localhost:4566 sqs send-message \
--queue-url http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/hybrid-queue \
--message-body "{\"id\":\"3\",\"name\":\"Lakshmi\",\"course\":\"HybridCloud\"}"
```
### Output Verification
Check Cloud SQL:
```sql
SELECT * FROM records;
```
Sample Output:

| id | name | course | processed_timestamp |
|:---|:---|:---|:---|
| 3 | Lakshmi | HybridCloud | 2026-04-29T18:06:26.344773 |

### Key Features
- Hybrid cloud architecture
- Multi-cloud communication
- Infrastructure as Code using Terraform
- Event-driven processing
- Automated data movement
- Real cloud database storage

### Challenges Faced
- Google Cloud authentication issues
- Cloud Function deployment permissions
- Terraform provider configuration
- Cloud SQL connectivity setup
- Folder structure alignment
All were resolved successfully.

### Conclusion
This project successfully demonstrates a production-style hybrid cloud data pipeline connecting LocalStack AWS services with Google Cloud services. It showcases practical cloud engineering, DevOps automation, and event-driven architecture skills.