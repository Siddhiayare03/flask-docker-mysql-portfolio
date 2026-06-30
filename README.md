# Flask Portfolio Website - DevOps Project

A full-stack portfolio website built using Flask and MySQL, containerized with Docker, deployed on AWS EC2, and automated using a Jenkins CI/CD pipeline.

---

## Project Overview

This project demonstrates an end-to-end DevOps workflow by building, containerizing, deploying, and automating a Flask web application.

The portfolio website allows visitors to submit messages through a contact form, which are stored in a MySQL database.

---

## Tech Stack

- Python
- Flask
- MySQL
- Docker
- Docker Compose
- Jenkins
- Git
- GitHub
- AWS EC2
- Ubuntu Linux

---

## Features

- Responsive Portfolio Website
- Contact Form
- MySQL Database Integration
- Dockerized Application
- Multi-container setup using Docker Compose
- Jenkins CI/CD Pipeline
- AWS EC2 Deployment

---

## Project Architecture

<img width="1536" height="1024" alt="ChatGPT Image Jul 1, 2026, 12_12_27 AM" src="https://github.com/user-attachments/assets/01e66999-0df8-4b5f-aa3d-ed493e43e222" />


---

## 📸 Screenshots

### Home Page

<img width="1521" height="690" alt="Screenshot 2026-06-30 233600" src="https://github.com/user-attachments/assets/0c4999e9-809d-4628-80c9-8b25e516d54e" />

<img width="1513" height="637" alt="Screenshot 2026-06-30 233612" src="https://github.com/user-attachments/assets/94573593-1f96-443d-8e7c-65484fa383e2" />

<img width="1522" height="693" alt="Screenshot 2026-06-30 233622" src="https://github.com/user-attachments/assets/d643dcc3-9a07-45ca-a434-47d2c67235bc" />

---

### Contact Form

<img width="1536" height="700" alt="Screenshot 2026-06-30 233657" src="https://github.com/user-attachments/assets/2dd15abf-d85d-4af7-962c-0d4e9691ca47" />

<img width="1536" height="529" alt="Screenshot 2026-06-29 215107" src="https://github.com/user-attachments/assets/71c96813-25f2-4935-8fc3-26199bd57874" />

---

### Jenkins Pipeline Success

<img width="751" height="667" alt="Screenshot 2026-06-30 235417" src="https://github.com/user-attachments/assets/b032dc05-bfc7-4ff2-840c-3960a01c7fb7" />

---

### Docker Containers Running

<img width="1503" height="176" alt="Screenshot 2026-06-30 235557" src="https://github.com/user-attachments/assets/9d40b69d-adbf-4002-9a90-1cf7f3bce49e" />

---

### AWS EC2 Deployment

<img width="1528" height="702" alt="Screenshot 2026-06-30 235846" src="https://github.com/user-attachments/assets/b4fa888b-fde7-433c-9d92-ade2e4fc7f21" />

<img width="758" height="558" alt="Screenshot 2026-06-30 235926" src="https://github.com/user-attachments/assets/947975d5-f904-460e-b0de-2e82017c2df1" />


---

## Project Structure

```text
flask-docker-mysql-portfolio/

├── app.py
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── profile.jpg
└── .gitignore
```

---

## Installation

```bash
git clone <https://github.com/Siddhiayare03/flask-docker-mysql-portfolio>

cd flask-docker-mysql-portfolio

docker compose up --build
```

Visit:

```
http://localhost:5000
```

---

## CI/CD Workflow

1. Developer pushes code to GitHub
2. Jenkins pulls the latest code
3. Docker builds the Flask application
4. Docker Compose starts Flask + MySQL containers
5. Application is deployed on AWS EC2

---

## Skills Demonstrated

- Docker
- Docker Compose
- Jenkins Pipelines
- CI/CD
- AWS EC2
- Git & GitHub
- Flask
- MySQL

---
## How to Run Locally

1. Clone the Repository
  git clone https://github.com/Siddhiayare03/flask-docker-mysql-portfolio.git

2. Navigate to the Project Directory
  cd flask-docker-mysql-portfolio

3. Make sure Docker Desktop is running

  Verify Docker installation:

  docker --version

  Verify Docker Compose:

  docker compose version

4. Build and Start the Containers
  docker compose up --build -d

  This command will:

  Build the Flask application image
  Pull the MySQL image (if not already available)
  Create both containers
  Create the Docker network
  Create the MySQL volume
  Start the application

5. Verify Running Containers
  docker ps

  Expected containers:
  
  flask-app
  mysql-db

6. Open the Portfolio Website

  Open your browser and visit:
  
  http://localhost:5000
  
  If deployed on AWS EC2:
  
  http://<EC2-Public-IP>:5000

7. Stop the Application
  docker compose down
  
  8. Rebuild After Code Changes
  
  If you make changes to the application:
  
  docker compose down
  docker compose up --build -d

9. View Container Logs 

  Flask logs:
  
  docker logs flask-app
  
  MySQL logs:
  docker logs mysql-db

---

## Future Improvements

- Kubernetes Deployment
- Terraform Infrastructure
- GitHub Actions
- Nginx Reverse Proxy
- HTTPS with SSL
- Monitoring using Prometheus & Grafana

---

## Author

Siddhi Ayare
