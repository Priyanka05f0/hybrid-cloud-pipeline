resource "aws_s3_bucket" "data_bucket" {
  bucket = "hybrid-data-bucket"
}

resource "aws_sqs_queue" "queue" {
  name = "hybrid-queue"
}

resource "aws_dynamodb_table" "records" {
  name         = "processed-records"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

resource "google_pubsub_topic" "topic" {
  name = "bridge-topic"
}