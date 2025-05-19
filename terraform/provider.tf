terraform {
  required_providers { 
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.113"
    }
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
