
The task will require the following items 

a Jenkins groovy file that creates jobs ( look for job DSL plugin ). Relevant for 1-3 questions

Items : 
 
Jenkins groovy file creates a pipeline job that pulls code from your GitHub repo.
       Build a docker container and push it to the docker hub. 

      The docker it builds is a python ( flask simple web application that talks to the local docker engine and gets the list of running containers ) 

Another job that takes a default Nginx docker file and modifies it and pushes a proxy pass to the first container (and injects
               in the request headers a source IP ) then push the container to docker hub  

A third job that runs the two containers and exposes the Nginx container ports only on the local Jenkins machine then sends
a request to verify the request has gone ok and finishes successfully.

Create a K8S cluster with at least one application that use volume and add Keda application and implement it on your application.
 

In the end, push everything to your GitHub project and send me the link.

--------------------------

# task #1:
pipeline that: 
- create jobs - DSL plugin

job1:
- agent pull code from github repo
- build docker container and push it to docker hub
  - container = python flask simple web app that talks to the local docker engine and gets the list of running containers

job2:
- take default nginx docker file, modify it + push proxy pass to 1st container + inject in request headers a source IP + push to docker hub

job3:
- runs 2 containers and exposes the nginx containers ports only on the local jenkins machine + send request to verify the request status ok and finish successfully

# task #2:
- create k8s cluster with one app that use volume and add keda app + implement it on the app

# task #3:
- push to github repo


repo/
├── seed-job.groovy          # DSL seed job that creates job1/2/3
├── jobs/
│   ├── job1.groovy
│   ├── job2.groovy
│   └── job3.groovy
├── flask-app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
└── k8s/
    ├── deployment.yaml      # app with PVC
    ├── pvc.yaml
    ├── keda-scaledobject.yaml
    └── (keda install notes or helm values)