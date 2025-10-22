import google.generativeai as genai
import streamlit as st
genai.configure(api_key="AIzaSyD3G__5I9EA9eHC3myDGEvj94uaEYwwkyM")
model=genai.GenerativeModel(model_name="gemini-2.5-flash-lite")
st.title("THE SELF-CARE SCAN")
st.subheader("A quick check-in for your mind and body.")
name=st.text_input("ENTER YOUR NAME:")
wt=st.number_input("ENTER YOUR WEIGHT IN KG:")
ht=st.slider("ENTER YOUR HEIGHT IN CM:",50,300)
age=st.number_input("ENTER YOUR AGE IN YEARS")
gender=st.selectbox("SELECT YOUR GENDER:",["male","female"])
bmi=round(wt/(ht/100)**2,2)
exercise=st.radio("How many hours in a day do you engage in physical activities( eg: yoga , swimming ,basketball etc.)?",["A) 0 ","B) 1 TO 2", "C)3 TO 4", "D)MORE THAN 4"])
st.write(f"you picked {exercise}")
st.write(f"{name}, your bmi is {bmi}")
sleep=st.radio("How many hours do you sleep at night?",["a) 2-4 hours","b) 4-6 hours","c) 6-8 hours","d) more than 8 hours"])
st.write(f"you picked {sleep}")
water=st.radio("How many glasses of water do you drink per day?",["a)2-4 glasses","b)4-6 glasses","c)6-8 glasses","d)8-10 glasses"])
st.write(f"you picked {water}")
veg=st.number_input("How much amount of fruits and vegetables do you consume per day approximately in gms?") 
stress=st.number_input("How many times in a month do you feel stressed?")
fgt=st.selectbox("Are you prone to forget things easily?",["never","rarely","often","sometimes"])
st.write(f"you picked {fgt}")
ph=st.selectbox("How often have you sought professional help for emotional or mental health issues?",["rarely","sometimes","often","no"])
prompt = f"act like an expert doctor ,comment on the health and the lifestyle to be followed with the following data: height as {ht},weight as {wt},exercise as {exercise}, sleep as {sleep},water intake as {water},stress feeling as {stress},vegetables and fruits intake as {veg},professional help for mental and emotional state as {ph},forget things easily as {fgt},and bmi as {bmi} as BMI is:"
response=model.generate_content(prompt)
st.markdown(response.text)



