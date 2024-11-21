
# Credit Card Default Prediction

This project aims to predict the likelihood of a client defaulting on their credit card payment next month using machine learning models. The project involves data cleaning, exploratory data analysis (EDA), feature engineering, and model training.

## Dataset
[Default of Credit Card Clients Dataset](https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip)



## Table of Contents
1. [Problem Definition](#problem-definition)
2. [Project Overview](#project-overview)
3. [Dataset Description](#dataset-description)
4. [Project Structure](#project-structure)
5. [Setup and Installation](#setup-and-installation)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [License](#license)

## Problem Definition

Credit card defaulting is a major risk for financial institutions. When clients fail to meet their payment obligations, it affects the profitability and sustainability of credit systems. Financial institutions require predictive systems to identify high-risk clients in advance, enabling them to make informed decisions such as adjusting credit limits, changing repayment plans, or taking preemptive actions.

This project addresses the problem of predicting credit card defaults by leveraging a dataset of 30,000 clients, containing their demographic information, credit history, and repayment patterns. The key objective is to develop a machine learning model that accurately predicts whether a client will default on their credit card payment in the following month.

### Business Significance
Accurate predictions can:
1. Reduce financial losses by proactively managing high-risk clients.
2. Optimize credit allocation and customer risk profiling.
3. Support strategic decision-making by providing actionable insights into repayment behaviors.

## Project Overview
Credit card defaults pose a significant risk to financial institutions. This project uses a dataset of credit card clients to build a predictive model for identifying potential defaults. The goal is to help financial institutions mitigate risk and make data-driven decisions.

## Dataset Description
The dataset contains information on 30,000 credit card clients in Taiwan from April to September 2005. It includes demographic details, billing information, and repayment status. The target variable is `default_payment`, indicating if a client will default next month.

### Key Features
- **Demographics**: Gender, age, education level, and marital status.
- **Credit and Billing**: Credit limit, past payments, and bill amounts.
- **Target**: Whether the client defaulted (1 = Yes, 0 = No).

For detailed information, refer to the [Data Dictionary](./Data_Dictionary.md).

## Project Structure
```
ML PROJECT/
│
├── data/                      # Contains the dataset
│   └── default of credit card clients.xls
│
├── environment_project/       # Folder with your model, scripts, and dependencies
│   ├── Pipfile                # Pipenv file for managing dependencies
│   ├── Pipfile.lock           # Lock file for consistent environments
│   ├── Dockerfile             # Dockerfile for running the service
│   ├── train.py               # Script for training and saving the model
│   ├── predict.py             # Script for serving predictions
│   ├── xgb_model.pkl          # Trained XGBoost model
│   ├── dv.pkl                 # DictVectorizer model
│   └── requirements.txt       # List of Python dependencies
│
├── data_dictionary.md         # Data dictionary
├── notebook.ipynb             # Jupyter notebook for EDA, model selection, and feature engineering
├── README.md                  # Project documentation

```

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/KipyegonH/mlzoomcamp_project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd 'ML PROJECT'
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the project in Docker (optional):
   ```bash
   docker build -t 'ML PROJECT' .
   docker run -p 9696:9696 'ML PROJECT'
   ```

## Usage
- **Train the model**:
  ```bash
  python src/train.py
  ```
- **Serve predictions**:
  ```bash
  python src/predict.py
  ```
- Access the web service at `http://localhost:5000`.

## Contributing
Contributions are welcome! Feel free to submit a pull request or report issues.


[def]: https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip