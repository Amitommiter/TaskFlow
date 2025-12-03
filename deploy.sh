#!/bin/bash

PROJECT_ID=${1:-"your-project-id"}
REGION=${2:-"us-central1"}

echo "Deploying to GCP Project: $PROJECT_ID"

gcloud config set project $PROJECT_ID

echo "Deploying App Engine application..."
gcloud app deploy app.yaml --quiet

echo "Deployment complete!"

