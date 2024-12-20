# MLOps - Cardiotocographs (CTGs)

This repository contains the practical exercise developed in the "Culture and Practices of DataOps and MLOps" course, part of the Specialization in Artificial Intelligence and Machine Learning at PUC Minas.

## Introduction

"Cardiotocography (CTG) is a non-invasive biophysical method for assessing fetal well-being. It involves the graphical recording of fetal heart rate and uterine contractions." - [Wikipedia](https://pt.wikipedia.org/wiki/Cardiotocografia)

The exam helps detect signs of fetal distress (when the fetus is not receiving enough oxygen during labor). If the exam results indicate a risk of fetal distress, additional measures can be taken to protect the health of the fetus and the mother.

## Objective

The objective of this practice is the creation of pipelines using a dataset that presents the main characteristics extracted from the exams.

The predictive model used classifies the exam readings into three classes:

- Normal: labor is progressing normally;
- Suspicious: the baby shows some signs of risk and requires special attention;
- Sick: the baby is already in fetal distress, and the delivery should be directed towards a cesarean section.


## Installation

- [Anaconda Python](https://www.anaconda.com/)
- [VSCode](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pt-br/pycharm/)
- [Docker Desktop](https://www.docker.com/)
- [Git Bash](https://git-scm.com/downloads)

## Run

- Access the project directory via terminal.
  
- Create the environment and install the necessary packages using the environment.yml file contained in the directory:
-  ```$ conda env create -f environment.yml```

- Activate the environment:
-  ```$ conda activate mlops_cardiotocografias_env```
  
- List the created environments:
-  ```$ conda env list```

  
- List the installed packages in the environment:
- ```$ pip freeze``` or ```$ pip list```

- Run ```$ python train.py```

## Other Conda Commands

- Update all packages in the environment:

- ```$ conda env update -f environment.yml```

## Accessing an Application with FastAPI

- Starting the server and creating documentation:

- ```$ uvicorn app.main:app --reload```

> ```Uvicorn``` is a high-performance ASGI (Asynchronous Server Gateway Interface) server for Python applications.

> ```app.``` is the directory.

> ```main``` is the name of the file (without the .py extension).

> ```:app``` is the name of the FastAPI instance in the code.

> The ```--reload``` flag makes the server automatically restart when there are changes in the code.

- In the browser:

- ```http://127.0.0.1:8000/docs```

## Create a Docker Image

- Create a ```Dockerfile``` that defines how to build your Docker image.
  
- Build the Docker image locally using ```$ docker build -t <image_name>```.
  
- Test the image locally with ```$ docker run -p <port>:<port> <image_name>```.
  
- Create a DockerHub account.
  
- Tag the image with your DockerHub username and repository name using ```$ docker tag <image_name> <username>/<repository>:<tag>```.
  
- Push the image to DockerHub using ```$ docker push <username>/<repository>:<tag>```.

## Create a Resource on Azure

- Create a signature.

- Create a new resource.

- Create a Container Instance and provide the DockerHub image details (image name and tag).

### Deploy the Container on Azure

- After configuring the container settings, create the resource.

- Azure will pull the image from DockerHub and deploy it as a container.

- Once the container is running, you can access your application through the assigned public IP address or domain.

## Load test

- Install Locust:

- ```$ sudo apt install python3-locust```

- In the main directory, run the ```locustfile.py``` program with the command:

- ```$ locust```

- Starting web interface at ```http://0.0.0.0:8089```

- Start the tests: Number of users: 100 users, Ramp up: 10 users and Host: container address in Azure.

