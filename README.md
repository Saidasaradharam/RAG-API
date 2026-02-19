
# Deploy a RAG API to Kubernetes

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-devops-kubernetes)

**Author:** Sai Dasaradharam  
**Email:** saidasaradharam9@gmail.com

---

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_y7z8a9b0)

---

## Introducing Today's Project!

I'm doing this project to learn how production systems manage containers at scale, specifically how Kubernetes handles deployment, networking, and automatic recovery so apps stay running reliably without manual intervention.

Kubernetes will help me orchestrate my RAG API containers by automatically restarting them if they crash, providing stable network access through Services, and giving me the foundation to scale the app when needed.

### Key services and concepts

Key concepts I learnt include that the kubernetes has pods which runs several containers and kubernetes service is used to redirect the api endpoin to the respective pod acting as a load balancer.


### Challenges and wins

The project took me approximately 90 minutes to complete as I had to understand how each and every part was working internally.


### Why I did this project

I did this project because I wanted to learn about docker and kubernetes.


---

## Setting Up My Docker Image

In this step, I'm setting up my Docker image, the packaged, portable version of my RAG API that contains all the code, dependencies, and configuration needed to run it.

I need a Docker image because Kubernetes can't run applications directly from source code. It needs a pre-built container image as its "instruction manual." 

Kubernetes takes that image and uses it to create and manage containers across the cluster. Without a Docker image, there's nothing for Kubernetes to deploy.

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_i9j0k1l2)

### What the Docker image contains

I ran docker images | Select-String "rag-app" and saw my rag-app image listed with the tag "latest", confirming it was successfully built.

### Docker image vs container

---

## Installing Kubernetes Tools

In this step, I'm installing two essential Kubernetes tools, Minikube and kubectl, and verifying that both are working correctly on my computer.
I need these tools because they work together to give me a complete local Kubernetes experience. Minikube creates and runs an actual Kubernetes cluster on my computer, so I don't need any cloud infrastructure or extra servers. 
kubectl is the command-line tool I use to interact with that cluster, letting me deploy applications, check the status of my pods, view logs, and manage everything from the terminal. Without Minikube, I have no cluster to deploy to. Without kubectl, I have no way to control or communicate with that cluster.

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_u1v2w3x4)

### Verifying the tools are installed

To install Minikube, I ran 
winget install -e --id Kubernetes.minikube 
which used Windows Package Manager to download and install Minikube automatically. I then verified it was installed correctly by running minikube version, which showed the installed version number.
To install kubectl, I ran 
winget install -e --id Kubernetes.kubectl 
which similarly used winget to install the Kubernetes command-line tool. I verified it with kubectl version --client, which displayed the client version and confirmed kubectl was ready to use.
Both tools were installed using winget, which is Windows' built-in package manager, making the process straightforward without needing to manually download installers.

### Minikube vs kubectl

---

## Starting My Kubernetes Cluster

In this step, I'm starting a local Kubernetes cluster using Minikube and verifying it is running correctly. I need a cluster because Kubernetes cannot work without one, it is the foundation that manages my RAG API containers, handling restarts, scaling, and networking automatically.

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_g3h4i5j6)

### Loading the Docker image into Minikube

I ran minikube start to create and start the local Kubernetes cluster. After it finished, I ran kubectl get nodes to verify the cluster was running, which showed my minikube node with a status of Ready, confirming the cluster was up and ready to deploy containers.

### Why load image into Minikube

I needed to load my Docker image into Minikube because Minikube runs in its own isolated environment, completely separate from my computer's Docker Desktop. So Kubernetes could not find the rag-app image from my local Docker storage.
To switch my terminal to use Minikube's Docker daemon, I ran
& minikube docker-env | Invoke-Expression. Then I rebuilt the image inside Minikube's environment using
docker build -t rag-app . 
so Kubernetes could find and use it when deploying my RAG API.

---

## Deploying to Kubernetes

In this stIn this step, I'm deploying my RAG API to Kubernetes by creating a Deployment using a deployment.yaml file. I need a Deployment because it acts as a blueprint that tells Kubernetes how to run my container, how many copies to run, and how to keep it running. If my container crashes, the Deployment automatically restarts it without any manual intervention.ep, I'm deploying... I need a Deployment because...

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_s5t6u7v8)

### How the Deployment keeps my app running

The deployment.yaml file tells Kubernetes how to run and manage my RAG API container inside the cluster. The key parts are the selector, template, and container specification, which all work together to create and maintain my running Pod.
The image field specifies rag-app as the Docker image Kubernetes should use to create the container, with imagePullPolicy: Never telling Kubernetes to use the locally available image instead of trying to pull it from Docker Hub.
The replicas field means Kubernetes will always keep exactly 1 copy of my RAG API running at all times. If the Pod crashes or is deleted, Kubernetes will automatically create a new one to maintain that desired state.

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_a3b4c5d6)

### What did you observe when checking your pods?

I ran kubectl get pods and saw my RAG API pod listed and running successfully. The pod had the name rag-app-deployment-xxxxxxxxx-xxxxx and status Running, which means Kubernetes successfully created the container from my rag-app image and it is actively running inside the cluster. The READY column showed 1/1, which indicates that 1 out of 1 container inside the pod is ready and healthy, meaning my RAG API is up and ready to receive traffic.

---

## Creating a Service

In this step, I'm creating a Kubernetes Service using a service.yaml file and verifying it is running correctly. I need a Service because my Pod's IP address changes every time it restarts, so I need a stable network endpoint to reliably access my RAG API. The Service acts as a consistent entry point that always routes traffic to the correct Pod, no matter how many times it gets recreated.

### What does the service.yaml file do?

The service.yaml file tells Kubernetes how to expose my RAG API so it can be accessed from outside the cluster. The selector finds Pods by matching the label app: rag-api, which connects the Service to the correct Pods created by my Deployment. The port configuration allows traffic coming in on port 8000 to be forwarded to port 8000 on the Pod, where my RAG API is listening. NodePort enables access from outside the cluster by opening a random port between 30000-32767 on the node, so I can send requests from my laptop directly to my RAG API running inside Kubernetes.

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_m5n6o7p8)

### What kubectl commands did you run to create the service?

I applied my Service file by running kubectl apply -f service.yaml, which told Kubernetes to create the Service defined in my service.yaml file. I then verified that the Service was created by running kubectl get services, which showed my rag-app-service listed with the type NodePort, confirming it was successfully created and ready to route traffic to my RAG API pods.

---

## Accessing My API Through Kubernetes

In this step, I'm testing my RAG API by accessing it through Kubernetes and sending it a real question to see if it returns an AI-generated response. I will use minikube service rag-app-service --url to get the URL of my running Service, then send a POST request to the API endpoint to verify that everything is working correctly, from the Service routing the traffic to the Pod processing the request and returning an answer.

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_y7z8a9b0)

### How I accessed my API

I tested my API by running Invoke-RestMethod -Uri "http://127.0.0.1:xxxxx/query?q=What is Kubernetes?" -Method POST in a new terminal window while keeping the Minikube tunnel open in the other terminal. The response showed a JSON object with an AI-generated answer about Kubernetes, confirming that the entire pipeline is working correctly, from the Service routing the request to the Pod, to ChromaDB retrieving the relevant context, to Ollama generating the final answer.
The main difference between Docker and Kubernetes deployment is that with Docker I would run the container manually and manage it myself, while Kubernetes automatically manages the container for me, handling networking through the Service, restarting the Pod if it crashes, and providing a stable endpoint to access my API regardless of what happens to the underlying container.

### Request flow through Kubernetes

The request flow went from my computer sending a POST request to the Minikube tunnel URL, then to the node which received the request on the NodePort and forwarded it to the Service on port 8000, then to the Pod where my RAG API container processed the request by searching ChromaDB for relevant context and sending it to Ollama to generate an answer. The Service routed traffic by using the selector app: rag-api to find the matching Pod and forward the request to it. NodePort enabled access from outside the cluster by opening a port on the node that my laptop could connect to, acting as the entry point that bridged my computer and the Kubernetes cluster.

---

## Testing Self-Healing

In this project extension, I'm demonstrating Kubernetes' self-healing capability by deliberately deleting a running Pod and watching Kubernetes automatically create a replacement to maintain the desired state of 1 replica.
Self-healing is important because in real production systems, containers can crash at any time due to hardware failures, memory leaks, or bugs. Without self-healing, someone would have to manually notice the problem and restart the container, causing downtime. Kubernetes eliminates this by constantly comparing the desired state with the actual state and automatically taking action to fix any difference, keeping applications running 24/7 without human intervention.

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_w8x9y0z1)

### What did you observe when you deleted the pod?

When I deleted the pod, I saw the status change from Running to Terminating to ContainerCreating to Running again. A new pod was created because my Deployment has replicas: 1, which tells Kubernetes to always maintain exactly 1 running Pod. The moment Kubernetes detected the Pod was deleted, its reconciliation loop kicked in, noticed the actual state of 0 pods did not match the desired state of 1 pod, and automatically created a replacement to fix that difference.

![Image](http://learn.nextwork.org/sincere_olive_mysterious_damson/uploads/ai-devops-kubernetes_sm3j8k9l)

### How the Service routed traffic to the new pod

Here's a sample answer:

The Service automatically discovered the new Pod and started routing traffic to it because the new Pod was created with the same label app: rag-api that the Service selector looks for. Kubernetes continuously watches for Pods matching that label and updates its list of endpoints automatically, so no manual configuration was needed.
Without Kubernetes this would have required someone to manually notice the crashed container, restart it, and update any routing or load balancer configuration to point to the new instance, causing downtime in the process.
Self-healing is critical in production because applications can fail at any time and users expect services to be available 24/7. Kubernetes handles failures automatically behind the scenes, so engineers don't need to monitor servers around the clock and manually restart containers every time something goes wrong.

---

---
