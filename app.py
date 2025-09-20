from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from typing import List

# Load saved objects
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")
model = joblib.load("model.pkl")

# define feature columns
cat_cols = ['CONTRACEPTIVE USE',
       'FAMILY HISTORY OF FIBROID', 'FREQUENT URINATION',
       'PELVIC PAIN', 'PCOS']
# numerical columns
num_cols = ['AGE', 'BMI', 'NUMBER OF CHILDREN']

# Define input schema
class InputData(BaseModel):
    BMI: float
    AGE: float
    NUMBER_OF_CHILDREN: float
    CONTRACEPTIVE_USE: str
    FAMILY_HISTORY_OF_FIBROID: str
    FREQUENT_URINATION: str
    PELVIC_PAIN: str
    PCOS: str

class BatchInput(BaseModel):
    data: List[InputData]

app = FastAPI(title="Fibroid Prediction API")



# Helper preprocessing function
def preprocess_input(df):
    # Scale numeric
    X_num = scaler.transform(df[num_cols])
    X_num = pd.DataFrame(X_num, columns=num_cols, index=df.index)

    # Encode categorical
    X_cat = encoder.transform(df[cat_cols])
    X_cat = pd.DataFrame(X_cat, columns=encoder.get_feature_names_out(cat_cols), index=df.index)

    # Combine
    X_processed = pd.concat([X_num, X_cat], axis=1)
    return X_processed

@app.get("/")
def root():
    return {"message": "Fibroid Prediction API is running! Go to /docs to test."}

#Single prediction endpoint
@app.post("/predict")
def predict(user_input: InputData):
    df = pd.DataFrame([user_input.dict()])
    df.rename(columns={"NUMBER_OF_CHILDREN": "NUMBER OF CHILDREN",
                       "CONTRACEPTIVE_USE": "CONTRACEPTIVE USE",
                        "FAMILY_HISTORY_OF_FIBROID": "FAMILY HISTORY OF FIBROID",
                        "FREQUENT_URINATION": "FREQUENT URINATION",
                        "PELVIC_PAIN": "PELVIC PAIN"
    }, inplace=True)
    X_processed = preprocess_input(df)
    pred = model.predict(X_processed)[0]
    return {"prediction": (pred)}

# Batch prediction endpoint
@app.post("/predict_batch")
def predict_batch(batch_input: BatchInput):
    df = pd.DataFrame([row.dict() for row in batch_input.data])
    df.rename(columns={"NUMBER_OF_CHILDREN": "NUMBER OF CHILDREN",
                       "CONTRACEPTIVE_USE": "CONTRACEPTIVE USE",
                        "FAMILY_HISTORY_OF_FIBROID": "FAMILY HISTORY OF FIBROID",
                        "FREQUENT_URINATION": "FREQUENT URINATION",
                        "PELVIC_PAIN": "PELVIC PAIN"
    }, inplace=True)
    X_processed = preprocess_input(df)
    preds = model.predict(X_processed)
    return {"predictions": preds.tolist()}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", port=8000, reload=True)
