import streamlit as st
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

sc = pickle.load(open('scalar.pkl', 'rb'))

model = pickle.load(open('linear_regr_model.pkl', 'rb'))

with open('happiness_score_predictor_about.txt', 'r') as f:
    markdown_text = f.read()

st.title('Happiness Score Predictor')

with st.sidebar:
    st.title('About')
    st.markdown(markdown_text)
    

score_placeholder = st.empty()

left_col, right_col = st.columns(2)

with left_col:
    social_support = st.slider('Social Support', min_value = 0.0, max_value = 1.0, value = 0.5, step = 0.001, format = '%.3f')
    freedom = st.slider('Freedom to make life choices', min_value = 0.0, max_value = 1.0, value = 0.5, step = 0.001, format = '%.3f')
    generosity = st.slider('Generosity', min_value = -1.0, max_value = 1.0, value = 0.5, step = 0.001, format = '%.3f')
    gdp = st.number_input('GDP per capita', step = 0.01, min_value = 0.01, value = 8000.00)

with right_col:
    corruption = st.slider('Perceptions of corruption', min_value = 0.0, max_value = 1.0, value = 0.5, step = 0.001, format = '%.3f')
    positive_affect = st.slider('Positive affect', min_value = 0.0, max_value = 1.0, value = 0.5, step = 0.001, format = '%.3f')
    negative_affect = st.slider('Negative affect', min_value = 0.0, max_value = 1.0, value = 0.5, step = 0.001, format = '%.3f')
    life_expectancy = st.number_input('Healthy life expectancy', 0, 100, value = 60)



features = np.array([
    np.log(gdp),
    social_support,
    life_expectancy,
    freedom,
    generosity,
    corruption,
    positive_affect,
    negative_affect
]).reshape(1, -1)

scaled_features = sc.transform(features)
prediction = model.predict(scaled_features)
score_placeholder.markdown(f"### Predicted Happiness Score: **{prediction[0]:.2f}**")

