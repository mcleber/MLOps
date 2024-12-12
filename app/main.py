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
