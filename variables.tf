variable "client_id" {
  description = "Client ID for the Lambda function"
  type        = string
}

variable "client_secret" {
  description = "Client Secret for the Lambda function"
  type        = string
}

variable "aws_region" {
  description = "AWS region"
  type        = string
}

variable "aws_access_key_id" {
  description = "AWS Access Key ID"
  type        = string
}

variable "aws_secret_access_key" {
  description = "AWS Secret Access Key"
  type        = string
}

variable "s3_bucket_name" {
  description = "S3 bucket name to store the Lambda zip"
  type        = string
}

variable "lambda_role_arn" {
  description = "ARN of the IAM role for the Lambda function"
  type        = string
}
variable "lambda_function_name" {
  description = "Lambda function name"
  type        = string
}


