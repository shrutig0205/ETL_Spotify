provider "aws" {
  region     = var.aws_region
  access_key = var.aws_access_key_id
  secret_key = var.aws_secret_access_key
}

variable "aws_region" {}
variable "aws_access_key_id" {}
variable "aws_secret_access_key" {}
variable "s3_bucket_name" {}
variable "lambda_role_arn" {}
variable "lambda_layer_arn" {} # Add this variable

resource "aws_s3_bucket_object" "lambda_zip" {
  bucket = var.s3_bucket_name
  key    = "etlSpotify.zip"
  source = "lambda_function.zip"
}

resource "aws_lambda_function" "etl_spotify" {
  function_name    = "etlSpotify"
  s3_bucket        = var.s3_bucket_name
  s3_key           = aws_s3_bucket_object.lambda_zip.key
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.9"  # Update the runtime according to your lambda
  role             = var.lambda_role_arn

  layers = [
    var.lambda_layer_arn
  ]

  environment {
    variables = {
      CLIENT_ID     = var.client_id
      CLIENT_SECRET = var.client_secret
    }
  }
}

output "lambda_function_name" {
  value = aws_lambda_function.etl_spotify.function_name
}
