import streamlit as st
import pandas as pd
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
import streamlit_pandas as sp

def app():

    colored_header(
    label = 'You are in Data :blue[Filtering] page',
    color_name = 'blue-70',
    description = ''
)
    @st.cache_data
    def data1():
        df = pd.read_csv('Cleaned_Store_data.csv')
        return df
    df = data1()
    def data2():
        df1 = pd.read_csv('Cleaned_Store_data2.csv')
        return df1
    df1 = data2()

    df['year_of_week'] = df1['year_of_week']
    df['day_of_week'] = df['day_of_week'].map({0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'saturday',6:'Sunday'})

    filter = dataframe_explorer(df)
    button = st.button('**SUBMIT**',use_container_width = True)
    if button:
        st.dataframe(filter,use_container_width = True,hide_index=True)