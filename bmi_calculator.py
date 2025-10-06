import google.generativeai as genai
import streamlit as st
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model=genai.GenerativeModel(model_name="gemini-2.5-flash-lite")
st.title("AI BASED BMI CALCULATOR-KNOW YOUR HEALTH APP")
# BMI CALCULATOR
# TAKE INPUTS FROM THE USER
name=st.text_input("ENTER YOUR NAME:")
wt=st.number_input("ENTER YOUR WEIGHT IN KG:")
ht=st.slider("ENTER YOUR HEIGHT IN CM",50,200)
age=st.number_input("ENTER YOUR AGE IN YEARS")
gender=st.text_input("ENTER YOUR GENDER:")
#CALCULATE THE BMI 
bmi=round(wt/(ht/100)**2,2)
st.write(f"{name}, your bmi is {bmi}")
prompt = f"act like an expert nutritionist,comment on the bmi with the following data: height as {ht},weight as {wt},and bmi as {bmi} as BMI is:"
response=model.generate_content(prompt)
st.markdown(response.text)


