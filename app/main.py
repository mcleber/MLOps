import os
import mlflow
import json
import uvicorn
import numpy as np
from pydantic import BaseModel
from fastapi import FastAPI

"""
    Creating an Application with FastAPI

    This FastAPI application is designed to provide endpoints for checking the health status 
    of the API and for making predictions related to fetal health. It has the following endpoints:

    1. GET /: Returns the health status of the API.
    2. POST /predict: Makes a prediction using a model (currently returning a placeholder value).
"""

# Initialize the FastAPI application with a custom title and tags for documentation
app = FastAPI(title="Fetal Health API",
                openapi_tags=[ 
                    {
                        "name": "Health",  # Tag for health-related endpoints
                        "description": "Get API health status"  # Description of the health tag
                    }, 
                    {
                        "name": "Prediction",  # Tag for prediction-related endpoints
                        "description": "Model prediction"  # Description of the prediction tag
                    }
                ])


def loaded_model():
    print("reading model...")
    MLFLOW_TRACKING_URI = 'https://dagshub.com/clebermoretti/mlops_cardiotocography.mlflow'
    MLFLOW_TRACKING_USERNAME = 'clebermoretti'
    MLFLOW_TRACKING_PASSWORD = 'c6b0c9924c4810d3edd0945b15c2d0a6f2125ff1'
    os.environ['MLFLOW_TRACKING_USERNAME'] = MLFLOW_TRACKING_USERNAME
    os.environ['MLFLOW_TRACKING_PASSWORD'] = MLFLOW_TRACKING_PASSWORD

    print("setting mlflow...")
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

    print("creating client...")
    client = mlflow.MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)

    print("getting registered model...")
    registered_model = client.get_registered_model('fetal_health')

    print("read model...")
    run_id = registered_model.latest_versions[-1].run_id
    logged_model = f'runs:/{run_id}/model'
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    print(loaded_model)
    return loaded_model

# Define a health check endpoint to check the status of the API
@app.get(path='/',
            tags=['Health'])
def api_health():
    """
    Health check endpoint to verify if the API is up and running.
    
    Returns:
        dict: A JSON response indicating the health status of the API.
    """
    return {"status": "healthy"}  # Returns a JSON response indicating the API is healthy

# Define a prediction endpoint to make predictions using a model
@app.post(path='/predict',
            tags=['Prediction'])
def predict():
    """
    Prediction endpoint to simulate making a model prediction.
    
    This is a placeholder function and currently returns a fixed prediction value (0).
    
    Returns:
        dict: A JSON response containing the prediction value.
    """
    return {"prediction": 0}  # Returns a prediction (in this case, just a placeholder value of 0)
