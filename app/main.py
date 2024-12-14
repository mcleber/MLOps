import os
import mlflow
from mlflow.exceptions import MlflowException
import json
import uvicorn
import numpy as np
from pydantic import BaseModel
from fastapi import FastAPI


class FetalHeathData(BaseModel):
    accelerations: float
    fetal_movement: float
    uterine_contractions: float
    severe_decelerations: float


app = FastAPI(title="Fetal Health API",
                openapi_tags=[ 
                    {
                        "name": "Health",  
                        "description": "Get API health status"  
                    }, 
                    {
                        "name": "Prediction",  
                        "description": "Model prediction"  
                    }
                ])


def load_model():
    print("reading model...")

    MLFLOW_TRACKING_URI = 'https://dagshub.com/clebermoretti/mlops_cardiotocography.mlflow'
    MLFLOW_TRACKING_USERNAME = 'clebermoretti'
    MLFLOW_TRACKING_PASSWORD = 'c6b0c9924c4810d3edd0945b15c2d0a6f2125ff1'
    
    os.environ['MLFLOW_TRACKING_USERNAME'] = MLFLOW_TRACKING_USERNAME
    os.environ['MLFLOW_TRACKING_PASSWORD'] = MLFLOW_TRACKING_PASSWORD

    print("setting mlflow...")

    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

    try:
        print("creating client...")
        client = mlflow.MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)

        print("getting registered model...")
        registered_model = client.get_registered_model('fetal_health')

        if not registered_model.latest_versions:
            raise ValueError("No versions found for the model 'fetal_health'.")

        print("reading model...")
        run_id = registered_model.latest_versions[-1].run_id
        logged_model = f'runs:/{run_id}/model'

        loaded_model = mlflow.pyfunc.load_model(logged_model)
        print("Model loaded successfully.")
        return loaded_model

    except MlflowException as e:
        print(f"Error interacting with MLflow: {e}")
    except ValueError as e:
        print(f"Model version error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


@app.get(path='/',
            tags=['Health'])
def api_health():
    return {"status": "healthy"}


@app.post(path='/predict',
            tags=['Prediction'])
def predict(request: FetalHeathData):
    loaded_model = load_model()

    received_data = np.array([
        request.accelerations,
        request.fetal_movement,
        request.uterine_contractions,
        request.severe_decelerations,
    ]).reshape(1, -1)

    print(received_data)
    print(loaded_model.predict(received_data))

    return {"prediction": 0}
