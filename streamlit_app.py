import streamlit as st
import pandas as pd

def ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level):
    # Calculate conversion rates for control and treatment groups
    control_rate = control_conversions / control_visitors
    treatment_rate = treatment_conversions / treatment_visitors

    # Calculate pooled standard error
    pooled_se = ((control_rate * (1 - control_rate)) / control_visitors + (treatment_rate * (1 - treatment_rate)) / treatment_visitors) ** 0.5

    # Calculate Z-score
    z_score = (treatment_rate - control_rate) / pooled_se

    # Determine critical Z-value based on confidence level
    if confidence_level == 90:
        critical_z = 1.645
    elif confidence_level == 95:
        critical_z = 1.96
    elif confidence_level == 99:
        critical_z = 2.576
    else:
        raise ValueError("Confidence level must be 90, 95, or 99.")

    # Compare Z-score to critical Z-value and return result
    if z_score > critical_z:
        return "Experiment Group is Better"
    elif z_score < -critical_z:
        return "Control Group is Better"
    else:
        return "Indeterminate"

# Streamlit app layout
st.title('A/B Test Hypothesis Test')
st.text('This app performs an A/B test and determines whether the experiment group is better,\nthe control group is better, or if the result is indeterminate.')

# User inputs
control_visitors = st.number_input('Enter the number of visitors in the control group:')
control_conversions = st.number_input('Enter the number of conversions in the control group:')
treatment_visitors = st.number_input('Enter the number of visitors in the treatment group:')
treatment_conversions = st.number_input('Enter the number of conversions in the treatment group:')
confidence_level = st.selectbox('Select the confidence level:', [90, 95, 99])

# Validate input values
if control_visitors != 0 and control_conversions != 0 and treatment_visitors != 0 and treatment_conversions != 0:
    # Run hypothesis test
    if st.button('Run Hypothesis Test'):
        result = ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)
        st.write('Result:', result)
else:
    st.warning("Please enter non-zero values for all input fields.")




