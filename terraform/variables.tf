variable "project_id" {}
variable "region" {
  default = "europe-west1"
}
variable "zone" {
  default = "europe-west1-b"
}
variable "admin_username" {
  default = "debian"
}
variable "public_ssh_key_path" {
  default = "~/.ssh/id_rsa.pub"
}
