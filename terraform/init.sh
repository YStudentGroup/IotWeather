#!/bin/bash
apt update -y
apt install -y git curl build-essential
curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
apt install -y nodejs
npm install -g pm2
