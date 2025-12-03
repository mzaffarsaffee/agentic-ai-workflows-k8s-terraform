#!/bin/bash
cd infra/terraform
terraform apply -auto-approve

cd ../k8s
kubectl apply -f .
