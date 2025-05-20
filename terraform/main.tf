provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

resource "google_compute_network" "vpc_network" {
  name = "vpc-ci-cd"
}

resource "google_compute_subnetwork" "subnet" {
  name          = "subnet-ci-cd"
  ip_cidr_range = "10.0.1.0/24"
  region        = var.region
  network       = google_compute_network.vpc_network.id
}

resource "google_compute_address" "public_ip" {
  name   = "ci-cd-ip"
  region = var.region
}

resource "google_compute_firewall" "default" {
  name    = "allow-ssh-http"
  network = google_compute_network.vpc_network.name

  allow {
    protocol = "tcp"
    ports    = ["22", "80", "443"]
  }

  source_ranges = ["0.0.0.0/0"]
}

resource "google_compute_instance" "vm" {
  name         = "ci-cd-vm"
  machine_type = "e2-medium"
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2004-lts"
    }
  }

  network_interface {
    network    = google_compute_network.vpc_network.id
    subnetwork = google_compute_subnetwork.subnet.id

    access_config {
      nat_ip = google_compute_address.public_ip.address
    }
  }

  metadata_startup_script = file("init.sh") # Installation automatique (Node.js, Git, PM2...)

  tags = ["http-server", "https-server"]

  metadata = {
    ssh-keys = "${var.admin_username}:${file(var.public_ssh_key_path)}"
  }
}

output "public_ip" {
  value = google_compute_address.public_ip.address
}
