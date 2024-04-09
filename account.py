import streamlit as st 

import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('pondering-68f74-963373eb66d4.json')
# firebase_admin.initialize_app(cred)

def app():

    st.title("Welcome to :violet[Login Page]")
    # st.write('Account')
    choice = st.selectbox('Login/Sign Up',['Login','Sign Up'])

    if choice == 'Login' :

        st.text_input("Email Id")
        st.text_input('Password',type='password')
        st.button("Submit to Login")

    else :

        email = st.text_input("Email Address")
        password = st.text_input('Password',type='password')
        username = st.text_input("Enter Your Name")

        if st.button("Create Account") :
            user = auth.create_user(email=email,password=password,uid=username)
            st.success("Account is created succesfull")
            st.balloons()


        
# https://www.youtube.com/watch?v=h-k4FBCkLDs 10:02