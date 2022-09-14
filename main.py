import streamlit as st
import urllib
from PIL import Image
import time
import numpy as npp
import tensorflow as tf
from tensorflow import keras
#from tensorflow.keras.preprocessing import image
import pandas as pd
import pickle

# loading in the model to predict on the data
pickle_in = open('model1 (1).pkl', 'rb')
Voting = pickle.load(pickle_in)


def welcome():
    return 'welcome all'
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(How_would_you_rate_todays_day , How_many_activities_did_you_do_today  , How_much_productive_were_you , How_many_things_bothered_you):  
   
    prediction = Voting.predict(
        [[How_would_you_rate_todays_day, How_many_activities_did_you_do_today, How_much_productive_were_you , How_many_things_bothered_you]])
    print(prediction)
    return prediction

def main():
    html_temp= '''
            <div>
            <center> <H1> Get your Mental Health Score! </H1> </center> </div>'''
    st.markdown(html_temp, unsafe_allow_html= True)
#@st.cache(allow_output_mutation= True, suppress_st_warning= True)
html_temp= '''
            <div>
            <center> <H3> Please enter the relevant data on a scale of 1-10. </H3> </center> </div>'''
      
How_would_you_rate_todays_day = st.text_input("How would you rate today's day", "Type Here")
How_many_activities_did_you_do_today = st.text_input("How many activities did you do today ", "Type Here")
How_much_productive_were_you  = st.text_input("How much productive were you ", "Type Here")
How_many_things_bothered_you = st.text_input("How many things bothered you ", "Type Here")

result =""
            
if st.button("Predict"):
        result = prediction(How_would_you_rate_todays_day, How_many_activities_did_you_do_today, How_much_productive_were_you , How_many_things_bothered_you)
st.success('The output is {}'.format(result))
     
if __name__=='__main__':
    main()        
