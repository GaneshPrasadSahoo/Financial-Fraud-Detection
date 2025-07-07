# 💸 Financial Fraud Detection Web App

This Streamlit-powered web application allows users to input transaction details and predict whether the transaction is **fraudulent** or **safe**, using a pre-trained machine learning model.

## 🚀 Features

- Real-time fraud prediction
- Detects both:
  - `isFraud`: Whether the transaction is fraudulent
  - `isFlaggedFraud`: Whether the transaction is flagged as suspicious
- Clean and intuitive UI using Streamlit
- Encoded transaction types for machine learning compatibility
- Integrated link for immediate reporting to the [cybercrime.gov.in](https://cybercrime.gov.in/Webform/Accept.aspx) portal

---

## 📦 Requirements

- Python 3.7+
- Packages:
  - `streamlit`
  - `pandas`
  - `scikit-learn`
  - `pickle` (comes built-in)

Install dependencies using:

```bash
pip install streamlit pandas scikit-learn
```

---

## 🧠 Model Info

The app uses a **multi-output classification model** trained to predict:
- `isFraud`: Indicates if the transaction is fraudulent
- `isFlaggedFraud`: Indicates if the transaction has been flagged as suspicious

The model file is stored as:  
```
multi_output_classifier_model.pkl
```

---

## 💻 How to Run

1. Clone the repository or copy the script to your local machine.
2. Make sure `multi_output_classifier_model.pkl` is in the same directory.
3. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🧾 Inputs

| Field               | Description                                     |
|--------------------|-------------------------------------------------|
| `Transaction Type` | Type of transaction (e.g., PAYMENT, TRANSFER)   |
| `Amount`           | Amount involved in the transaction              |
| `Old Balance Org`  | Original account balance before transaction     |
| `New Balance Orig` | Account balance after the transaction           |
| `Old Balance Dest` | Recipient account balance before transaction    |

---

## ✅ Output

After submitting the transaction details, the model predicts:

- **isFraud**: `True` / `False`
- **isFlaggedFraud**: `True` / `False`

🟢 If both are `False`:  
✅ *“No fraud detected. Your transaction is secure.”*

🔴 If `isFraud = True`:  
⚠️ *“Your transaction is fraudulent. Contact 1930 immediately.”*  
🔗 A link to [cybercrime.gov.in](https://cybercrime.gov.in/Webform/Accept.aspx) is provided for lodging a complaint.

🟠 If `isFlaggedFraud = True` but `isFraud = False`:  
⚠️ *“Suspicious activity detected. Please contact 1930.”*

---

## 🎨 UI and Style

The app includes custom CSS styling for:
- Headings
- Predict button
- Hover effects for better UX

---

## 📌 Note

- Ensure the `LabelEncoder` categories match the types used in model training.
- The app will raise an error if unexpected types or missing values are encountered.

---

## 🛡️ Disclaimer

This tool is for **educational and demonstration purposes** only. For real-world fraud detection, always rely on professional financial security services.
