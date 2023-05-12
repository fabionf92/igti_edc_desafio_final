## backend configuration requires an AWS storage bucket

terraform {
  backend "s3" {
    bucket = "terraform-state-igti-fabio"
    key    = "igti/edc/desafio-final/terraform.tfstate"
    region = "us-east-2"
  }
}