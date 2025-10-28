## Q1 - Install uv
1. pip install uv
2. uv --version
3. mkdir 05-deployment
4. cd 05-deployment
5. uv init

## Q2 - Install scikit-learn==1.6.1
1. uv add scikit-learn==1.6.

## Q3  - Load model and predict
1. uv run python score.py

## Q4 - Serve the model with FastAPI
1. uv add fastapi uvicorn requests
2. uv run uvicorn service:app --host 0.0.0.0 --port 8000
3. uv add requests
4. uv run python client.py

## Q5 - Docker base image
1. docker pull agrigorev/zoomcamp-model:2025
2. docker 

## Q6 - Containerize and serve the 
1. create a dockerfile
2. docker build -t zoomcamp-service:v1 .
3. docker run -it --rm -p 8000:8000 zoomcamp-service:v1
4. uv run python test_docker.py