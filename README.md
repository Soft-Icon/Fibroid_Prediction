# Fibroid Prediction

This project aims to develop a predictive model for identifying the presence of fibroids using medical data. The repository contains code, data processing scripts, and documentation to facilitate reproducible research and deployment.

## Features

- Data preprocessing and cleaning
- Exploratory data analysis (EDA)
- Machine learning model training and evaluation
- Visualization of results

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Soft-Icon/Fibroid_Prediction.git
    cd Fibroid_Prediction
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Run API
``bash
uvicorn main:app --reload
``

## Project Structure

```
Fibroid_pred/
├── data/
├── notebooks/
├── app.py          # the fastAPI code base
├── model.pkl
├── encoder.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```
## API Endpoints
1. Single prediction
- URL:
```/predict
```              
- Method: POST
- Description: Accepts patient data and returns a fibroid prediction ("No" Fibroid, "Yes" Fibroid).

2. Batch predictions
- URL: 
```/predict-batch
```
- Method: POST
- Description: Accepts a list of patients and returns predictions for each.

## Request JSON Example:
1. Single Prediction
```
    json
{
  "BMI": 24.5,
  "AGE": 32,
  "NUMBER_OF_CHILDREN": 2,
  "CONTRACEPTIVE_USE": "Yes",
  "FAMILY_HISTORY_OF_FIBROID": "No",
  "FREQUENT_URINATION": "Yes",
  "PELVIC_PAIN": "No",
  "PCOS": "No"
}
```

Response:
```
{
  "predictions": ["Yes", "No"]
}

```
2. Batch Predictions
```
    json
{
  "data": [
    {
      "BMI": 24.5,
      "AGE": 32,
      "NUMBER_OF_CHILDREN": 2,
      "CONTRACEPTIVE_USE": "Yes",
      "FAMILY_HISTORY_OF_FIBROID": "No",
      "FREQUENT_URINATION": "Yes",
      "PELVIC_PAIN": "No",
      "PCOS": "No"
    },
    {
      "BMI": 30.1,
      "AGE": 40,
      "NUMBER_OF_CHILDREN": 3,
      "CONTRACEPTIVE_USE": "No",
      "FAMILY_HISTORY_OF_FIBROID": "Yes",
      "FREQUENT_URINATION": "No",
      "PELVIC_PAIN": "Yes",
      "PCOS": "Yes"
    }
  ]
}
```
response:
{
  "predictions": ["Yes", "No"]
}

## API Documentation (alternative)
fastAPI provides interactive documentation
- Swagger UI
```
https://fibroid-prediction.onrender.com/docs
```
or check out

- ReDoc
```
https://fibroid-prediction.onrender.com/redoc
```

## Authentication
Authentication is not enabled (will be in the future)

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.