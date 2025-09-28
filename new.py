import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
import numpy as np

@st.cache_data
def load_data_and_train_model():
    df = pd.read_csv('college_student_placement_dataset.csv')
    df_model = df[['IQ', 'CGPA', 'Internship_Experience', 'Placement']].copy()

    le = LabelEncoder()
    df_model['Internship_Experience'] = le.fit_transform(df_model['Internship_Experience'])
    df_model['Placement'] = le.fit_transform(df_model['Placement'])

    X = df_model[['IQ', 'CGPA', 'Internship_Experience']]
    y = df_model['Placement']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    clf = LogisticRegression()
    clf.fit(X_train_scaled, y_train)

    return clf, scaler, df

st.set_page_config(page_title="Student Placement Predictor", layout="wide")

st.title('🎓 Student Placement Predictor')
st.write("This web app predicts whether a student will be placed based on their academic performance and experience. The model is trained on a dataset of college students.")

clf, scaler, df = load_data_and_train_model()

st.sidebar.header('👤 Input Student Data')

def user_input_features():
    iq = st.sidebar.slider('IQ', 80, 150, 100)
    cgpa = st.sidebar.slider('CGPA', 5.0, 10.0, 7.5, 0.1)
    internship = st.sidebar.selectbox('Internship Experience', ('Yes', 'No'))

    data = {
        'IQ': iq,
        'CGPA': cgpa,
        'Internship_Experience': 1 if internship == 'Yes' else 0
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader('Your Input:')
st.write(input_df)


if st.button('🔮 Predict Placement'):
    input_scaled = scaler.transform(input_df)
    
    prediction = clf.predict(input_scaled)
    prediction_proba = clf.predict_proba(input_scaled)

    st.subheader('Prediction Result:')
    
    if prediction[0] == 1:
        st.success(f"**High Chance of Placement**")
        st.write(f"Confidence: **{prediction_proba[0][1]*100:.2f}%**")
    else:
        st.error(f"**Low Chance of Placement**")
        st.write(f"Confidence: **{prediction_proba[0][0]*100:.2f}%**")

if st.checkbox('Show Raw Data'):
    st.subheader('Dataset Used for Training')
    st.write(df)
