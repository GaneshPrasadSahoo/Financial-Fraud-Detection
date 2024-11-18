import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the model
with open('multi_output_classifier_model.pkl', 'rb') as file:
    clf = pickle.load(file)

# Initialize LabelEncoder and fit it with the correct categories
label_encoder = LabelEncoder()
label_encoder.fit(['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])

# Define the expected column order based on your model training
expected_columns = ['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest']

# Streamlit App
st.markdown('<h1 style="text-align: center; color: #FF5733;">Financial Fraud Detection</h1>', unsafe_allow_html=True)

# User inputs
st.markdown("<h1 style='text-align: center; color: #008000;'>Transaction Details</h1>", unsafe_allow_html=True)
# Create columns for layout
col1, col2 = st.columns(2)

with col1:
    type_value = st.selectbox('Transaction Type', ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])
    amount = st.number_input('Amount', value=181.00)
    oldbalanceOrg = st.number_input('Old Balance Org', value=181.0)

with col2:
    newbalanceOrig = st.number_input('New Balance Orig', value=0.0)
    oldbalanceDest = st.number_input('Old Balance Dest', value=0.0)

# Prepare input for prediction
def preprocess_input(type_value, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest):
    # Convert type to encoded value
    encoded_type = label_encoder.transform([type_value])[0]
    
    # Create DataFrame for prediction
    sample_input = pd.DataFrame({
        'type': [encoded_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest]
    })
    
    # Ensure sample_input has the same columns and order as expected
    sample_input = sample_input[expected_columns]
    
    return sample_input

# Make predictions
if st.button('Predict', key='predict', help='Click to make a prediction'):
    try:
        sample_input = preprocess_input(type_value, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest)
        predictions = clf.predict(sample_input)
        
        # Convert numeric predictions (1, 0) to boolean (True, False)
        is_fraud = bool(predictions[0][0])  # 1 -> True, 0 -> False
        is_flagged_fraud = bool(predictions[0][1])  # 1 -> True, 0 -> False
        
        st.write('Verdict:')
        st.write(f'isFraud: {is_fraud}')
        st.write(f'isFlaggedFraud: {is_flagged_fraud}')
        
        # Fraud detection logic based on the predictions
        if is_fraud and not is_flagged_fraud:
            st.error("Your transaction is fraudulent. Contact 1930 immediately.")
            st.write("Visit the link and complain: [cybercrime.gov.in](https://cybercrime.gov.in/Webform/Accept.aspx)")
        elif is_fraud and is_flagged_fraud:
            st.error("Your transaction is fraudulent. Contact 1930 immediately.")
            st.write("Visit the link and complain: [cybercrime.gov.in](https://cybercrime.gov.in/Webform/Accept.aspx)")
        elif not is_fraud and is_flagged_fraud:
            st.warning("Suspicious activity detected in your transaction. Please contact 1930.")
            st.write("Visit the link and complain: [cybercrime.gov.in](https://cybercrime.gov.in/Webform/Accept.aspx)")
        else:
            st.success("No fraud detected. Your transaction is secure.")
        
    except Exception as e:
        st.error(f"Error during prediction: {e}")

# Custom CSS for button size and hover effect
st.markdown("""
    <style>
    .css-1emrehy.edgvbvh3 {
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        font-size: 18px;
        padding: 12px 24px;
        transition: background-color 0.3s;
    }
    .css-1emrehy.edgvbvh3:hover {
        background-color: #0056b3;
    }
    </style>
    """, unsafe_allow_html=True)
