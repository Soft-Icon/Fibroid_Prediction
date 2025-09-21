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
    git clone https://github.com/Soft-Icon/Fibroid_pred.git
    cd Fibroid_pred
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

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
Endpoint                    Method                  Description
- ```/predict```              POST                    Single Prediction
- ```/predict-batch```        POST                    Batch predictions

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.