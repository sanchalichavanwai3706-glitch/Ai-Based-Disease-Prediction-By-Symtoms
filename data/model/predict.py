import pandas as pd

# Load dataset
data = pd.read_csv('data/dataset.csv')

# Function to predict disease
def predict_disease(symptoms):
    for index, row in data.iterrows():
        if (symptoms[0] == row['symptom1'] and
            symptoms[1] == row['symptom2'] and
            symptoms[2] == row['symptom3']):
            return row['disease']
    return "Disease not found"

# Take input from user
print("Enter 3 symptoms:")
s1 = input("Symptom 1: ")
s2 = input("Symptom 2: ")
s3 = input("Symptom 3: ")

# Predict
result = predict_disease([s1, s2, s3])

print("\nPredicted Disease:", result)
