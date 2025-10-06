import google.generativeai as genai
import streamlit as st
genai.configure(api_key="AIzaSyD3G__5I9EA9eHC3myDGEvj94uaEYwwkyM")
model=genai.GenerativeModel(model_name="gemini-2.5-flash-lite")
st.title("AI BASED BMI CALCULATOR-KNOW YOUR HEALTH APP")
# BMI CALCULATOR
# TAKE INPUTS FROM THE USER
name=input("ENTER YOUR NAME:")
wt=int(input("ENTER YOUR WEIGHT IN KG:"))
ht=int(input("ENTER YOUR HEIGHT IN CM"))
