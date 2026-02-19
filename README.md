<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Deploy a RAG API to Kubernetes

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-devops-kubernetes)

**Author:** Sai Dasaradharam  
**Email:** saidasaradharam9@gmail.com

---

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_y7z8a9b0)

---

## Introducing Today's Project!

### Key services and concepts

Key concepts I learnt include that the kubernetes has pods which runs several containers and kubernetes service is used to redirect the api endpoin to the respective pod acting as a load balancer.


### Challenges and wins

The project took me approximately 90 minutes to complete as I had to understand how each and every part was working internally.


### Why I did this project

I did this project because I wanted to learn about docker and kubernetes.


---

## Setting Up My Docker Image

### What the Docker image contains

### Docker image vs container

---

## Installing Kubernetes Tools

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_u1v2w3x4)

### Verifying the tools are installed

### Minikube vs kubectl

---

## Starting My Kubernetes Cluster

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_g3h4i5j6)

### Loading the Docker image into Minikube

### Why load image into Minikube

---

## Deploying to Kubernetes

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_s5t6u7v8)

### How the Deployment keeps my app running

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_a3b4c5d6)

### What did you observe when checking your pods?

---

## Creating a Service

### What does the service.yaml file do?

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_m5n6o7p8)

### What kubectl commands did you run to create the service?

---

## Accessing My API Through Kubernetes

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_y7z8a9b0)

### How I accessed my API

### Request flow through Kubernetes

---

## Testing Self-Healing

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_w8x9y0z1)

### What did you observe when you deleted the pod?

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_sm3j8k9l)

### How the Service routed traffic to the new pod

---

---
