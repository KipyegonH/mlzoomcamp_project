import pickle
import xgboost as xgb
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the model and DictVectorizer
with open('xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('dv.pkl', 'rb') as f:
    dv = pickle.load(f)

# Preprocessing function to ensure data consistency
def preprocess_input_data(data):
    # Mapping categorical columns to strings (same as during training)
    sex_values = {1: 'male', 2: 'female'}
    data['sex'] = sex_values.get(data['sex'], 'unknown')

    education_values = {1: 'graduate school', 2: 'university', 3: 'high school', 4: 'others', 0: 'others', 5: 'others', 6: 'others'}
    data['education'] = education_values.get(data['education'], 'others')

    marriage_values = {1: 'married', 2: 'single', 3: 'others', 0: 'others'}
    data['marriage'] = marriage_values.get(data['marriage'], 'others')

    pay_values = {
        -2: 'not paid duly', -1: 'pay duly', 0: 'no delay', 1: 'payment delay for one month',
        2: 'payment delay for two months', 3: 'payment delay for three months',
        4: 'payment delay for four months', 5: 'payment delay for five months',
        6: 'payment delay for six months', 7: 'payment delay for seven months',
        8: 'payment delay for eight months', 9: 'payment delay for nine months and above'
    }
    for pay_col in ['pay_0', 'pay_2', 'pay_3', 'pay_4', 'pay_5', 'pay_6']:
        data[pay_col] = pay_values.get(data.get(pay_col), 'no delay')

    # Ensure all string columns are lowercased and spaces replaced with underscores (same as training step)
    for col, value in data.items():
        if isinstance(value, str):
            data[col] = value.lower().replace(' ', '_')

    return data

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Check if the data is wrapped in a list and extract the dictionary
    if isinstance(data, list):
        data = data[0][0][0]  # Extract the first item from the list
    # Preprocess the input data
    processed_data = preprocess_input_data(data)
    
    # Transform the data using the DictVectorizer
    data_transformed = dv.transform(processed_data)
    
    # Create DMatrix for prediction
    dmatrix = xgb.DMatrix(data_transformed, feature_names=dv.get_feature_names_out().tolist())
    
    # Make the prediction
    prediction = model.predict(dmatrix)
    
    # Return the prediction result
    return jsonify({'prediction': float(prediction[0])})

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
