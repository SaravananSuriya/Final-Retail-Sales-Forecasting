import streamlit as st
from streamlit_extras.colored_header import colored_header

def app():
    # st.write('dfdsff')
    colored_header(
    label = 'Welcome to :orange[Home] Page 👋🏼',
    color_name = 'orange-70',
    description = '',
)
    with st.form(key = 'form',clear_on_submit=False):

        st.markdown("## :orange[*Project title*:]")
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *Final Retail Sales Forecasting*")
        st.markdown("## :orange[*Skills take away From This Project*:]")
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *Python scripting, Data Wrangling, EDA, Model Building, Streamlit.*")
        st.markdown("## :orange[*Domain*:]")
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *Supermarkets, Chain and Convenience Stores.*")
        st.markdown("## :orange[*Problem Statement:*]")
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *Predict the department-wide sales for each store for the following year and the Model effects of markdowns on holiday weeks.*")
        st.markdown("## :orange[*Results:*]")
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *In this project Utilizing advanced time series forecasting models, successfully predicted department-wide sales for each store for the upcoming year. The forecasting model considered historical sales data, seasonality patterns, and other relevant factors to provide accurate and reliable predictions*")
        # st.markdown("## :orange[*Dataset:*]")
        button = st.form_submit_button('**Click here to get Data Set Link**',use_container_width = True)
        if button:
            url = "https://drive.google.com/drive/u/0/folders/1-DX3a7-jraKDIPhJY1HNBSt5E4sA5hmb"
            st.markdown("## :orange[Dataset : [Data Link](%s)]"% url)