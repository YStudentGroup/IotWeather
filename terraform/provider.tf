
terraform {
  required_providers { 
    azurerm    = {
      source   = "hashicorp/azurerm"
      version  = "~> 3.113"
    }
  }
  backend "azurerm" {
    resource_group_name   = var.backend_rg_name
    storage_account_name  = var.backend_account_name 
    container_name        = var.backend_container_name 
    key                   = "terraform.tfstate"
    access_key            = var.backend_access_key
  }
}

Configuration du provider Azure,
provider "azurerm" {
  features {}
}