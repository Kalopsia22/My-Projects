#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
os.environ['NUMEXPR_MAX_THREADS'] = '4'
os.environ['NUMEXPR_NUM_THREADS'] = '2'


# In[12]:


import json
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_lottie import st_lottie
import requests


# ## Animations

# In[13]:
st.set_page_config(page_title="Curricular Vitae (CV)", page_icon=":tada:", layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# In[14]:
lottie_url1 = "https://assets7.lottiefiles.com/packages/lf20_bR3P9F.json"
lottie_json1 = load_lottieurl(lottie_url1)
lottie_url2 = "https://assets2.lottiefiles.com/packages/lf20_DMgKk1.json"
lottie_json2 = load_lottieurl(lottie_url2)
lottie_url3 = "https://assets1.lottiefiles.com/packages/lf20_0tue65cn.json"
lottie_json3 = load_lottieurl(lottie_url3)
lottie_url4 = "https://assets5.lottiefiles.com/packages/lf20_qkekrsxe.json"
lottie_json4 = load_lottieurl(lottie_url4)
lottie_url5 = "https://assets6.lottiefiles.com/packages/lf20_es4p9zph.json"
lottie_json5 = load_lottieurl(lottie_url5)
lottie_url6 = "https://assets6.lottiefiles.com/packages/lf20_vnikrcia.json"
lottie_json6 = load_lottieurl(lottie_url6)
lottie_url7 = "https://assets6.lottiefiles.com/packages/lf20_xafe7wbh.json"
lottie_json7 = load_lottieurl(lottie_url7)
lottie_url8 = "https://assets4.lottiefiles.com/packages/lf20_tno6cg2w.json"
lottie_json8 = load_lottieurl(lottie_url8)
lottie_url9 = "https://assets4.lottiefiles.com/packages/lf20_ngzwzxib.json"
lottie_json9 = load_lottieurl(lottie_url9)
lottie_url10 = "https://assets10.lottiefiles.com/private_files/lf30_oOGQFY.json"
lottie_json10 = load_lottieurl(lottie_url10)
# In[15]:


##lottie_url2 = "https://assets2.lottiefiles.com/packages/lf20_DMgKk1.json"
##lottie_json2 = load_lottieurl(lottie_url2)


# ## CSS 
# 

# In[16]:


def local_css(style):
    with open(style) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
local_css("style.css")




# In[17]:


st.title("Atharva Rewatkar")
st.subheader("A fragment quivering without rhythm in the sphere of life....")
st.write("\n")
st.write("\n")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Designations ~")
        st.write("\n")
        st.subheader(":diamond_shape_with_a_dot_inside: An AI & ML Enthusiast :computer:")
        st.write("\n")
        st.subheader(":diamond_shape_with_a_dot_inside: Author of the Anthology 'Petrichor of My Love' :gift_heart:")
        st.write(":sparkling_heart: Link to my book :arrow_right:")
        st.write("\n") 
        st.subheader("Ex- AIML Intern at Percept Infosystems")
        st.write("\n") 
    
    with right_column:
        st_lottie(lottie_json1, height=400, key=None)


with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Education ~")
        st.write("\n")
        
        st.subheader("Higher Secondary")
        st.write("Taywade Junior College")
        st.write("\n")
        
        st.subheader("Bachelor of Technology in CSE(AI&ML)")
        st.write("Shri Ramdeobaba College of Engineering and Management")
        st.write("\n")  
    
    with right_column:
        st_lottie(lottie_json2, height=400, key=None)


with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("My Projects ~")
        st.write("\n")
        st.write("[All projects so far:arrow_right:](https://github.com/Kalopsia22/My-Projects)"  )
    
    with right_column:
        st_lottie(lottie_json3, height=250, key=None)


with st.container():
    left_column, right_column= st.columns(2)
    with left_column:
        st.title("Certifications ~")
        st.write("\n")
        st.subheader("Non-Technical Certificates")
        st.write(":diamond_shape_with_a_dot_inside: Introduction to Criminology")
        st.write(":diamond_shape_with_a_dot_inside: Narcissistic Behaviour & Relationships")
        st.write(":diamond_shape_with_a_dot_inside: Psychology of Criminal Behaviour & Criminology")
        st.write(":diamond_shape_with_a_dot_inside: Certificate  on Body Languageand Psychology")
        st.write(":diamond_shape_with_a_dot_inside: Diploma in Modern Applied Psychology")
        st.write(":diamond_shape_with_a_dot_inside: Marketing Psychology")
        st.write(":diamond_shape_with_a_dot_inside: PSYCHOLOGY DIPLOMA")
        st.write(":diamond_shape_with_a_dot_inside: Stress & Anxiety Management")
        st.write("\n")
        st.write("[Link to Certificates:arrow_right:](https://github.com/Kalopsia22/Courses_Certificates/tree/main/Non-Technical%20Courses)")
        st.write("\n")
    
    with right_column:
        st_lottie(lottie_json4, height=400, key=None)
    
    with st.container():
        left_column, right_column= st.columns(2)
        with left_column:
            st.subheader("Technical Certificates")
            st.write("\n")
            
            st.subheader(":white_large_square: Amazon Web Services")
            st.write(":diamond_shape_with_a_dot_inside: AWS Cloud Technical Essentials")
            st.write(":diamond_shape_with_a_dot_inside: Addressing Security Risk")
            st.write(":diamond_shape_with_a_dot_inside: Building Serverless Applications")
            st.write("\n")
            
            st.subheader(":white_large_square: Basics of Block Chain")
            st.write(":diamond_shape_with_a_dot_inside: Blockchain Basics")
            st.write(":diamond_shape_with_a_dot_inside: Smart Contracts")
            st.write(":diamond_shape_with_a_dot_inside: DAPPS")
            st.write("\n")
            
            st.subheader(":white_large_square: Computer Networks")
            st.write(":diamond_shape_with_a_dot_inside: The Complete Networking Fundamentals")
            st.write("\n")
            
            st.subheader(":white_large_square: Full Stack")
            st.write(":diamond_shape_with_a_dot_inside: 100 Days of Code The Complete Python Pro Bootcamp for 2023")
            st.write(":diamond_shape_with_a_dot_inside: Google Course Certificate")
            st.write(":diamond_shape_with_a_dot_inside: The Complete 2022 Web Development Bootcamp")
            st.write(":diamond_shape_with_a_dot_inside: The Complete DSA")
            st.write("\n")
            
            st.subheader(":white_large_square: Microsoft Azure")
            st.write(":diamond_shape_with_a_dot_inside: Introduction to Microsoft Azure Cloud Services")
            st.write(":diamond_shape_with_a_dot_inside: Microsoft Azure Management Tools and Security Solutions")
            st.write(":diamond_shape_with_a_dot_inside: Microsoft Azure Services and Lifecycles")
            st.write(":diamond_shape_with_a_dot_inside: Data Storage in Microsoft Azure")
            st.write("\n")
            
            st.subheader(":white_large_square: Database Management Systems")
            st.write(":diamond_shape_with_a_dot_inside: Database Management System from scratch - Part 1")
            st.write(":diamond_shape_with_a_dot_inside: Database Management System from scratch - Part 2")
            st.write(":diamond_shape_with_a_dot_inside: Database Management Systems Part 3")
            st.write(":diamond_shape_with_a_dot_inside: Database Management System from scratch - Part 4")
            st.write(":diamond_shape_with_a_dot_inside: Database Management Final Part (5)")
            st.write("\n")
            
            st.write("[Link to Certificates:arrow_right:](https://github.com/Kalopsia22/Courses_Certificates/tree/main/Technical%20Courses)")
        with right_column:
            st_lottie(lottie_json5, height=400, key=None)
            st_lottie(lottie_json6, height=250, key=None)
            st_lottie(lottie_json7, height=400, key=None)

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Skills ~")
        st.write("\n")
        
        st.subheader(":white_large_square: DevOps")
        st.write(":diamond_shape_with_a_dot_inside: Streamlit")
        st.write(":diamond_shape_with_a_dot_inside: Firebase and Firestore")
        st.write(":diamond_shape_with_a_dot_inside: Apache Airflow")
        st.write("\n")
        
        st.subheader(":white_large_square: Cloud Computing")
        st.write(":diamond_shape_with_a_dot_inside: Microsoft Azure Storage")
        st.write(":diamond_shape_with_a_dot_inside: Amazon Web Services")
        st.write("\n")
        
        st.subheader(":white_large_square: Frontend Development")
        st.write(":diamond_shape_with_a_dot_inside: HTML")
        st.write(":diamond_shape_with_a_dot_inside: CSS and Bootstrap")
        st.write(":diamond_shape_with_a_dot_inside: JavaScript")
        st.write("\n")

        st.subheader(":white_large_square: Backend Development")
        st.write(":diamond_shape_with_a_dot_inside: Python3")
        st.write(":diamond_shape_with_a_dot_inside: Have knowledge in AI, ML, Deep Learning and NLP")
        st.write(":diamond_shape_with_a_dot_inside: SQL")
        st.write("\n")

        st.subheader(":white_large_square: SEO and Content Writing")
        st.write("\n")

        st.subheader(":white_large_square: Finance and Data Analytics")
        st.write(":diamond_shape_with_a_dot_inside: Microecnomics")
        st.write(":diamond_shape_with_a_dot_inside: Macroecnomics and Government Policies")
        st.write(":diamond_shape_with_a_dot_inside: Microsoft Excel")
        st.write("\n")
    
    with right_column:
        st_lottie(lottie_json8, height=250, key=None)
        st.write("\n")
        st.write("\n")
        st_lottie(lottie_json9, height=250, key=None)
        st.write("\n")
        st.write("\n")
        st_lottie(lottie_json10, height=250, key=None)

with st.container():
    st.write("---")
    st.header("Get in contact!")
    st.write("\n")
    st.write("##")
    st.write("\n")
    contact_form = """ 
    my mail:arrow_right: redolent.souvenirs@gmail.com
     <input type="hidden" name= "_captcha" value= "false">
     <br></br>
     <input type="text" name="name" placeholder="Your name" required>
     <br></br>
     <input type="email" name="email" placeholder="Your email" required>
     <br></br>
     <textarea name = "message" placeholder= "Your Message here" required></textarea>
     <br></br>
     <button type="submit">Send</button>
</form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()