# Home Assignment - Elbit DevOps

## Overview
Definition of jenkins pipeline using DSL plugin of Jenkins, Docker, k8s with Keda autoscaling.

---

## Repository Structure
├── flask-app/         
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile.multistage
│   └── .dockerignore
├── nginx/              # Custom Nginx reverse proxy
│   ├── Dockerfile
│   └── nginx-lb.conf
├── jenkins/            # Jenkins pipeline definitions
│   ├── seed_job.groovy # Seed job that generates job1, job2, job3
│   └── jobs/
│       ├── job1.groovy
│       ├── job2.groovy
│       └── job3.groovy
└── k8s/                # Kubernetes manifests
├── deployment.yaml
├── pvc.yaml
├── service.yaml
└── keda-scaledobject.yaml

---

## Part 1 - Jenkins + Docker

- **Flask app** exposes '/containers' endpoint - lists running Docker containers + 'health'
- **Nginx** is used as a reverse proxy in front of Flask, injecting 'X-Forwarded-For' and 'X-Real-IP' header
- **Jenkins** is used to build and deploy the app
- **JOb1** builds and pushes the flask image to docker hub
- **JOb2**  builds and pushed the nginx imagem (custom) to docker hub
- **JOb3** runs both containers, check health and clean up

### Prerequisites
- Jenkins running locally with Docker access:
```bash
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts

docker exec -u root jenkins bash -c "apt-get update && apt-get install -y docker.io"
docker exec -u root jenkins bash -c "chmod 666 /var/run/docker.sock"
```

- Plugins required: **Job DSL**
- Credentials required:
  - `github-creds` – GitHub username + Personal Access Token
  - `docker-creds` – Docker Hub username + password

### Running the pipeline
1. Create a new Pipeline job in Jenkins named `seed-job`
2. Use the following script:
```groovy
node {
    git url: 'https://github.com/elisacoh/home-assignment-elbit.git',
        credentialsId: 'github-creds',
        branch: 'main'
    jobDsl targets: 'jenkins/seed_job.groovy'
}
```
3. Run `seed-job` → it generates `job1-build-flask`, `job2-build-nginx`, `job3-integration-test`
4. Run the jobs in order: job1 → job2 → job3

### Docker Hub Images
- `elcosah/flaskapp-elbit:latest`
- `elcosah/nginx-elbit:latest`


## Part 2 – Kubernetes + KEDA

