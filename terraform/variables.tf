variable "admin_username" {
  default = "Seb"
}

variable "ssh_public_key_path" {
  default = "terraform/id_rsa.pub"
}

variable "resource_group_name" {
  default = "Seb-RG"
}

variable "location" {
  description = "La région Azure où les ressources seront déployées"
  default     = "France Central"
}

variable "backend_container_name" {
  description = "Nom du conteneur de stockage pour le backend Terraform"
}

variable "backend_rg_name" {
  description = "Nom du groupe de ressources pour le backend Terraform"
}

variable "backend_account_name" {
  description = "Nom du compte de stockage pour le backend Terraform"
}


variable "backend_access_key" {
  description = "Clé d'accès pour le compte de stockage du backend Terraform"
}

variable "admin_password" {
  description = "Clé d'accès pour le compte de stockage du backend Terraform"
}