#!/bin/bash
# Simple bash script to create SSL certificate and private key non-interactively.
# -nodes -x509 tell means do not encrypt the private key and we want an x509 cert.
# The key.pem and cert.pem outputs are stored in the ssl/directory.


mkdir - p ssl
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 \
    -subj "/C=US/ST=Louisiana/L=Baton Rouge/O=RG-Networks/CN=nms.rg-networks.net" \
    -keyout ssl/key.pem -out ssl/cert.pem
