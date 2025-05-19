terraform {
  required_providers { 
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.113"
    }
  }
  backend "azurerm" {
    resource_group_name  = "Seb-RG"
    storage_account_name = "sebterraformstorage"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
    access_key           = var.backend_access_key
  }
}

provider "azurerm" {
  features {}
}

variable "backend_access_key" {
  description = "Clé d'accès au Storage Account pour le backend"
  type        = string
  sensitive   = true
}
