
from django.shortcuts import render
from joblib import load
import pandas as pd

# Load your trained model
model = load('./savedModels/models.joblib')

# Create your views here.
def predictor(request):
    return render(request, 'main.html')

def fromInfo(request):
    # Extract query parameters
    Gender = request.GET['Gender']
    Married = request.GET['Married']
    Dependents = request.GET['Dependents']
    Education = request.GET['Education']
    Self_Employed = request.GET['Self_Employed']
    ApplicantIncome = request.GET['ApplicantIncome']
    CoapplicantIncome = request.GET['CoapplicantIncome']
    LoanAmount = request.GET['LoanAmount']
    Loan_Amount_Term = request.GET['Loan_Amount_Term']
    Credit_History = request.GET['Credit_History']
    Property_Area = request.GET['Property_Area']

    # Define the feature names used during training
    feature_names = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
                     'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
                     'Credit_History', 'Property_Area']

    # Prepare the input data
    input_data = {
        'Gender': [Gender],
        'Married': [Married],
        'Dependents': [Dependents],
        'Education': [Education],
        'Self_Employed': [Self_Employed],
        'ApplicantIncome': [ApplicantIncome],
        'CoapplicantIncome': [CoapplicantIncome],
        'LoanAmount': [LoanAmount],
        'Loan_Amount_Term': [Loan_Amount_Term],
        'Credit_History': [Credit_History],
        'Property_Area': [Property_Area]
    }

    # Convert input data to DataFrame with the correct feature names
    input_df = pd.DataFrame(input_data, columns=feature_names)

    # Make predictions using the correctly formatted input data
    y_pred = model.predict(input_df)
    if y_pred[0]=="N":
       y_pre="No"
    elif y_pred[0]=="Y":
        y_pre="Yes"
    else:
        y_pre="Can Not Say"
    print(y_pre)
    # Render the result template with the prediction
    return render(request, 'result.html', {'name': y_pre})
