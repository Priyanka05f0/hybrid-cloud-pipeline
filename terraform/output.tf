output "s3_bucket_name" {
  value = aws_s3_bucket.data_bucket.bucket
}

output "sqs_queue_url" {
  value = aws_sqs_queue.queue.id
}

output "pubsub_topic" {
  value = google_pubsub_topic.topic.name
}