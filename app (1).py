import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showfileUploaderEncoding', False)
# Load the pickled model
pickle_in = open("/content/drive/My Drive/decision_model.pkl","rb")
model=pickle.load(pickle_in)

def predict_note_authentication(age ,hypertension,heart_disease, avg_glucose_level,bmi,smoking_status):
  output= model.predict([[age ,hypertension,heart_disease, avg_glucose_level,bmi,smoking_status]])
  print("Purchased", output)
  if output==[1]:
    prediction="He will have stroke"
  else:
    prediction="He will not have stroke"
  print(prediction)
  return prediction
def main():
    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">OdinSchool</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Course on streamlit</p></center> 
   <center><p style="font-size:25px;color:white;margin-top:10px;"> Project Deployment</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.header("Stroke Prediction")
    age = st.number_input("age",18,60)
    hypertension = st.number_input("hypertension",0,122)
    heart_disease = st.number_input("heart_disease",0,99)
    avg_glucose_level= st.number_input("avg_glucose_level",0,846)
    bmi= st.number_input("bmi",0,68)
    smoking_status= st.number_input("smoking_status",0,67)
    resul=""
    if st.button("Predict"):
      result=predict_note_authentication(age ,hypertension,heart_disease, avg_glucose_level,bmi,smoking_status)
      st.success('Model has predicted {}'.format(result))
    if st.button("About"):
      st.subheader("Developed by Dr.Megha Gupta")
      st.subheader(" Developer")

if __name__=='__main__':
  main()
   
