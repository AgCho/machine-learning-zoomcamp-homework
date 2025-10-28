import pickle
from pathlib import Path
from fastapi import FastAPI

app = FastAPI()

# model is baked into the base image here:
candidates = [Path("/code/pipeline_v2.bin"), Path("pipeline_v2.bin")]

model_path = next((p for p in candidates if p.exists()), None)
if model_path is None:
    raise FileNotFoundError("pipeline_v2.bin not found (checked /code and current dir)")

with model_path.open("rb") as f_in:
    pipeline = pickle.load(f_in)

@app.post("/predict")
def predict(client_data: dict):
    proba = pipeline.predict_proba([client_data])[0, 1]
    return {"probability": round(float(proba), 2)}
