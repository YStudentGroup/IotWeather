#!/bin/bash

sudo apt update -y
sudo apt install -y git python3-pip

cd /home/${USER}

# Supprimer si déjà existant
rm -rf api
git clone https://github.com/TON_ORG/api-repo.git api
cd api

pip install -r requirements.txt

# Lancer ton API (FastAPI exemple)
nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
