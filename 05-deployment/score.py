import pickle
import json
import sys
from pathlib import Path

MODEL_PATH = Path("pipeline_v1.bin")

def main():
    # Record to score
    record = {
        "lead_source": "paid_ads",
        "number_of_courses_viewed": 2,
        "annual_income": 79276.0
    }

    # Load pipeline
    with MODEL_PATH.open("rb") as f_in:
        pipeline = pickle.load(f_in)

    # The pipeline expects a list of dicts
    proba = pipeline.predict_proba([record])[0, 1]

    # Print raw and rounded
    print(f"probability={proba:.6f}")
    print(f"rounded_to_3dp={proba:.3f}")

if __name__ == "__main__":
    main()