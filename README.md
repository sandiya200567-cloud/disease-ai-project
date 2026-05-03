# Explainable AI Disease Prediction System

## Overview

This project predicts diseases based on symptoms using a Machine Learning model and provides explanation along with a chatbot response.

## Features

* Disease prediction using Decision Tree
* Explanation of prediction
* Chatbot assistance
* Flask API backend
* Docker containerization

## Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* Docker

## How to Run

### Run Locally

python app.py

### Run Using Docker

docker build -t disease-ai .
docker run -p 5000:5000 disease-ai

## API Endpoint

POST /predict

### Example Input

{
"fever": 1,
"cough": 1,
"fatigue": 1
}

## Output

* Predicted Disease
* Explanation
* Chatbot Response

## SDG Goal

Supports United Nations Sustainable Development Goal 3:
Good Health and Well-being

## Limitations

* Small dataset
* Not a replacement for medical professionals
