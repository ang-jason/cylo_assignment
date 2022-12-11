terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.54"
    }
  }

  backend "s3" {
    region  = "ap-southeast-1"
    bucket  = "terraform-state-bucket-jason"
    key     = "s3-backend.tfstate"
    encrypt = true
  }

  # backend "local" {
  # path = "./local.terraform.tfstate"
  # }


}

provider "aws" {
  region = "ap-southeast-1"
}