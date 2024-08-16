# Spotify ETL Pipeline using AWS Lambda and Terraform

![Spotify ETL Pipeline](https://github.com/user-attachments/assets/6dd6b7cf-1bde-4adc-81eb-0fe37a6b2cb1)

This project implements a fully automated ETL (Extract, Transform, Load) data pipeline for Spotify using AWS Lambda, Terraform, and GitHub Actions. The pipeline is designed to extract data from the Spotify Web API, transform it, and load it into an S3 bucket for further analysis.

## Features
- **AWS Lambda Functions**: Automated extraction, transformation, and loading of Spotify data.
- **Terraform**: Infrastructure as Code (IaC) to provision and manage AWS resources.
- **GitHub Actions**: CI/CD pipeline for continuous integration and deployment.
- **S3 Storage**: Secure storage of transformed data in AWS S3.

## Project Structure
```plaintext
.
├── extract_spotify_data.py               # Extracts data from Spotify API
├── transform_spotify_data.py             # Transforms the extracted data
├── load_spotify_data_.py                 # Loads the transformed data to S3
├── main.tf                               # Terraform configuration file
├── variables.tf                          # Terraform variables
├── .github/
│   └── workflows/
│       └── deploy_lambda.yml             # GitHub Actions workflow for deployment
├── requirements.txt                      # Python dependencies
└── README.md                             # Project README
```
## Prerequisites
- **Python 3.12**: Ensure you have Python 3.12 installed.
- **AWS Account**: Set up an AWS account to deploy the Lambda functions.
- **Terraform**: Install Terraform to manage AWS resources.
- **GitHub Actions**: CI/CD integration requires setting up GitHub Actions.




