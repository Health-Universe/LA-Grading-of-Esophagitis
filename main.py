import streamlit as st
import pandas as pd
import numpy as np

# Define Los Angeles (LA) Grading of Esophagitis
def calculate_LA_grading(esophageal_mucosal_breaks):
    if esophageal_mucosal_breaks <= 5:
        return "Grade A"
    elif esophageal_mucosal_breaks <= 10:
        return "Grade B"
    elif esophageal_mucosal_breaks <= 15:
        return "Grade C"
    else:
        return "Grade D"

# Layout the app
st.title("Los Angeles (LA) Grading of Esophagitis Calculator")
st.write("""
This app calculates the Los Angeles (LA) Grading of Esophagitis based on the number of esophageal mucosal breaks. Please note that the grading is a simplification of the actual criteria.

Here are the grading categories:

- Grade A: One (or more) mucosal break no longer than 5mm that does not extend between the tops of two mucosal folds
- Grade B: One (or more) mucosal break more than 5mm long that does not extend between the tops of two mucosal folds
- Grade C: One (or more) mucosal break that is continuous between the tops of two or more mucosal folds but which involve less than 75% of the esophageal circumference
- Grade D: One (or more) mucosal break which involve at least 75% of the esophageal circumference
""")

# Get user input
esophageal_mucosal_breaks = st.slider("Enter the number of esophageal mucosal breaks (mm)", 1, 20, 1)

# Calculate and display the LA Grading of Esophagitis
result = calculate_LA_grading(esophageal_mucosal_breaks)
st.write("The Los Angeles (LA) Grading of Esophagitis is: ", result)
