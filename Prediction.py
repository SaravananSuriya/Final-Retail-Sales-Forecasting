import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header
import pandas as pd
import pickle

def app():
    colored_header(
    label = 'Welcome to Data :red[Prediction] page 👋🏼',
    color_name = 'red-70',
    description = 'Weekly Sales Prediction for the following year'
)

    @st.cache_data
    def data():
        df = pd.read_csv('Cleaned_Store_data2.csv')
        return df
    df = data()
    x = df.drop(['Size','Type','Date','weekly_sales'],axis = 1)

    # st.dataframe(x.head())

    with st.form(key = 'form',clear_on_submit=False):
        
        store = st.selectbox(
                "**Select a Store**",
                options = df['Store'].unique(),
            )
        
        dept = st.selectbox(
                "**Select a Department**",
                options = df['Dept'].unique(),
            )
        
        holiday = st.radio(
                "**Click Holiday is True or False**",
                options = [True, False],
                horizontal = True
            )

        temperature = st.number_input(
                f"**Enter a Temperature in range of (Minimum : {df['Temperature'].min()} & Maximum : {df['Temperature'].max()})**",
               
            )

        fuel = st.number_input(
                f"**Enter a Fuel Price in range of (Minimum : {df['Fuel_Price'].min()} & Maximum : {df['Fuel_Price'].max()})**",
              
            )

        cpi = st.number_input(
                f"**Enter a Customer Price Index in range of (Minimum : {df['CPI'].min()} & Maximum : {df['CPI'].max()})**",
              
            )

        unemployment = st.number_input(
                f"**Enter a Unemployment in range of (Minimum : {df['Unemployment'].min()} & Maximum : {df['Unemployment'].max()})**",
               
            )

        year = st.selectbox(
                "**Select a Year**",
                options = df['year'].unique(),
            )

        yearofweek = st.selectbox(
                "**Select Year of Week**",
                options = df['year_of_week'].unique(),
            )

        markdown = st.number_input(
                f"**Enter a Markdown value in range of (Minimum : {df['Markdown'].min()} & Maximum : {df['Markdown'].max()})**",
               
            )

        def inv_trans(x):
            if x == 0:
                return x
            else:
                return 1/x
        inv_trans(markdown)

        def is_holiday(x):
            if x == True:
                return 1
            else:
                return 0
        is_holiday(holiday)

        with open('model.pkl', 'rb') as file:
                model = pickle.load(file)
        result = model.predict([[store, dept, is_holiday(holiday), temperature, fuel, cpi, unemployment, year, yearofweek, inv_trans(markdown)]])

        button = st.form_submit_button('**Predict**',use_container_width = True)
        if button == True:
            st.markdown(f"## :green[*Predicted Weekly Sales is {result}*]")
