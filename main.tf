provider "aws" {
  region     = var.aws_region
}

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
  runtime          = "python3.12" 
  role             = var.lambda_role_arn

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
