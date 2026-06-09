# ML API Deployment on AWS using Docker, ECR, EC2, ALB, Auto Scaling & CI/CD

## Overview

This project demonstrates how to package a Machine Learning API inside a Docker container and deploy it on AWS using production-style infrastructure.

The primary goal of this project is to learn and implement a complete MLOps/DevOps workflow, including:

- Containerization with Docker
- Private container registry using Amazon ECR
- Deployment on Amazon EC2
- Application Load Balancer (ALB)
- Auto Scaling Group (ASG)
- Automated CI/CD using GitHub Actions
- Cloud-native architecture for scalable ML inference services

---

## Architecture

```text
Developer
    |
    | Git Push
    v
GitHub Repository
    |
    | GitHub Actions
    v
Docker Build
    |
    v
Amazon ECR
    |
    v
Auto Scaling Group
    |
    v
EC2 Instances
    |
    | Docker Pull & Run
    v
FastAPI Application
    |
    v
Application Load Balancer
    |
    v
End Users
```

---

## Technology Stack

### Backend

- Python 3.10
- FastAPI
- Uvicorn

### Containerization

- Docker

### AWS Services

- Amazon EC2
- Amazon ECR
- Application Load Balancer (ALB)
- Auto Scaling Group (ASG)
- IAM Roles
- CloudWatch

### CI/CD

- GitHub Actions

---

## Project Structure

```text
ML-env/
│
├── app.py
├── model.py
├── requirements.txt
├── Dockerfile
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
└── README.md
```

---

## API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "ML API is running"
}
```

---

### Prediction Endpoint

```http
POST /predict
```

Request:

```json
{
  "features": [1, 2, 3]
}
```

Response:

```json
{
  "prediction": 3.0
}
```

---

## Running Locally

### Clone Repository

```bash
git clone <repository-url>
cd ML-env
```

---

### Build Docker Image

```bash
docker build -t ml-api .
```

---

### Run Container

```bash
docker run -p 8000:8000 ml-api
```

---

### Access Swagger UI

```text
http://localhost:8000/docs
```

---

## Docker Image

Build image:

```bash
docker build -t ml-api .
```

Verify image:

```bash
docker images
```

Run container:

```bash
docker run -d -p 8000:8000 ml-api
```

Check running containers:

```bash
docker ps
```

---

## Amazon ECR Setup

Login:

```bash
aws ecr get-login-password --region us-east-1 \
| docker login \
--username AWS \
--password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
```

Tag image:

```bash
docker tag ml-api:latest \
<account-id>.dkr.ecr.us-east-1.amazonaws.com/ml-api:latest
```

Push image:

```bash
docker push \
<account-id>.dkr.ecr.us-east-1.amazonaws.com/ml-api:latest
```

---

## EC2 Deployment

### Install Docker

```bash
sudo dnf update -y
sudo dnf install docker -y

sudo systemctl start docker
sudo systemctl enable docker

sudo usermod -aG docker ec2-user
```

---

### Pull Image

```bash
docker pull \
<account-id>.dkr.ecr.us-east-1.amazonaws.com/ml-api:latest
```

---

### Run Container

```bash
docker run -d -p 8000:8000 \
<account-id>.dkr.ecr.us-east-1.amazonaws.com/ml-api:latest
```

---

## Auto Scaling Deployment

The project uses:

- Launch Template
- Auto Scaling Group
- Application Load Balancer

### Auto Scaling Configuration

```text
Minimum Capacity : 2
Desired Capacity : 2
Maximum Capacity : 5
```

Scaling Policy:

```text
Target CPU Utilization: 60%
```

---

## Launch Template User Data

Each new EC2 instance automatically:

1. Installs Docker
2. Starts Docker service
3. Authenticates with ECR
4. Pulls latest image
5. Runs Docker container

Example User Data:

```bash
#!/bin/bash

dnf update -y
dnf install docker -y

systemctl start docker
systemctl enable docker

aws ecr get-login-password --region us-east-1 \
| docker login --username AWS \
--password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

docker pull <account-id>.dkr.ecr.us-east-1.amazonaws.com/ml-api:latest

docker run -d -p 8000:8000 \
<account-id>.dkr.ecr.us-east-1.amazonaws.com/ml-api:latest
```

---

## CI/CD Pipeline

The deployment pipeline is fully automated using GitHub Actions.

Workflow:

```text
Git Push
    |
    v
GitHub Actions
    |
    v
Docker Build
    |
    v
Push Image to ECR
    |
    v
Trigger Auto Scaling Group Refresh
    |
    v
Deploy New Version
```

---

## GitHub Actions Workflow

Location:

```text
.github/workflows/deploy.yml
```

Pipeline Tasks:

- Checkout source code
- Configure AWS credentials
- Login to ECR
- Build Docker image
- Push image to ECR
- Trigger Auto Scaling Group refresh

---

## Monitoring

CloudWatch can be used for:

- CPU utilization monitoring
- Memory monitoring
- Network monitoring
- Auto Scaling metrics
- Application logs

Recommended alarms:

- CPU > 80%
- Memory > 80%
- Unhealthy targets > 0
- Instance count changes

---

## Future Improvements

- Blue/Green Deployment
- Canary Releases
- AWS ECS Migration
- AWS EKS (Kubernetes)
- MLflow Integration
- S3 Model Registry
- Prometheus Monitoring
- Grafana Dashboards
- HTTPS with ACM Certificates
- WAF Protection
- Secrets Manager Integration

---

## Learning Objectives

This project demonstrates practical experience with:

- Docker Containerization
- AWS Infrastructure
- MLOps Fundamentals
- CI/CD Automation
- High Availability Systems
- Auto Scaling Architecture
- Production Deployment Patterns

---

## Disclaimer

This project was created as a learning exercise to understand end-to-end deployment of Machine Learning APIs on AWS using modern DevOps and MLOps practices. It is intended for educational and experimentation purposes and can be extended into a production-grade deployment with additional security, monitoring, and governance controls.