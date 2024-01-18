import streamlit as st
import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
import plotly.express as px

def app():
    colored_header(
    label = 'You are in Data :green[Analysis] page',
    color_name = 'green-70',
    description = ''
)
    @st.cache_data
    def dataframe():
        df = pd.read_csv('Cleaned_Store_data.csv')
        # df1 = pd.read_csv('Cleaned_Store_data2.csv')
        return df
    df = dataframe()
    def dataframe1():
        # df = pd.read_csv('Cleaned_Store_data.csv')
        df1 = pd.read_csv('Cleaned_Store_data2.csv')
        return df1
    df1 = dataframe1()

    choice = st.selectbox("**Select an option to Explore their data**", (['Explore of Weekly Sales','Explore of Markdown']))

    if choice == 'Explore of Weekly Sales':

        st.markdown("## :rainbow[Stores and their sum of Weekly Sales]")
        sales = df.groupby(['Store'])['Weekly_Sales'].sum().reset_index()#.sort_values('Weekly_Sales',ascending=False).head(10)
        # st.dataframe(sales)
        st.bar_chart(sales, x = 'Store', y = 'Weekly_Sales')

        st.markdown("## :rainbow[Top 10 Store has Highest Sales]")
        highest_sale = df.groupby(['Store'])['Weekly_Sales'].sum().reset_index().sort_values('Weekly_Sales',ascending=False).head(10)
        st.bar_chart(highest_sale, x = 'Store', y = 'Weekly_Sales', color = '#04f')

        st.markdown("## :rainbow[Top 10 Store has Lowest Sales]")
        lowest_sale = df.groupby(['Store'])['Weekly_Sales'].sum().reset_index().sort_values('Weekly_Sales',ascending=True).head(10)
        st.bar_chart(lowest_sale, x = 'Store', y = 'Weekly_Sales',color = '#fd0')


        st.markdown("## :rainbow[Department and their sum of Weekly Sales]")
        sales = df.groupby(['Dept'])['Weekly_Sales','Store'].sum().reset_index()#.sort_values('Weekly_Sales',ascending=False).head(10)
        # st.dataframe(highest_sale)
        st.bar_chart(sales, x = 'Dept', y = 'Weekly_Sales')

        st.markdown("## :rainbow[Top 10 Department has Highest Sales]")
        highest_sale = df.groupby(['Dept'])['Weekly_Sales'].sum().reset_index().sort_values('Weekly_Sales',ascending=False).head(10)
        st.bar_chart(highest_sale, x = 'Dept', y = 'Weekly_Sales', color = '#3F00FF')

        st.markdown("## :rainbow[Top 10 Department has Lowest Sales]")
        lowest_sale = df.groupby(['Dept'])['Weekly_Sales'].sum().reset_index().sort_values('Weekly_Sales',ascending=True).head(10)
        st.bar_chart(lowest_sale, x = 'Dept', y = 'Weekly_Sales', color = '#CCCCFF')

        st.markdown("## :rainbow[Sum of weekly sales with their year]")
        total_year = df.groupby('year')['Weekly_Sales'].sum().reset_index()
        # st.dataframe(total_year)
        pie = px.pie(total_year, values = 'Weekly_Sales',names = 'year',width=900,height=500)
        st.plotly_chart(pie)

        col,col1 = st.columns([2,2])
        with col:    
            radio = st.radio('**Select a Year to Analyze with that year**', options = df['year'].unique(), horizontal = True)
        with col1:
            select = st.selectbox("**Select any feature**", (['Temperature','Fuel_Price','CPI','Unemployment']))       
        

        st.markdown(f"## :rainbow[{select} vs Sales]")
        data = df[df['year'] == radio]
        dataframe = data.groupby(select)['Weekly_Sales'].sum().reset_index()
        hist = px.histogram(dataframe, x = select,y = 'Weekly_Sales', width = 1050)
        st.plotly_chart(hist)

        date = st.selectbox("**Select a feature to explore periodic wise**", (['month','day','day_of_week','year_of_week']))

        st.markdown(f"## :rainbow[{date} vs Sales]")
        df['year_of_week'] = df1['year_of_week']
        df['day_of_week'] = df['day_of_week'].map({0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'saturday',6:'Sunday'})
        data = df[df['year'] == radio]
        dataframe = data.groupby(date)['Weekly_Sales'].sum().reset_index()
        st.bar_chart(dataframe, x = date,y = 'Weekly_Sales')

        st.markdown(f"## :rainbow[Date vs Sales]")
        data = df[df['year'] == radio]
        date = data.groupby('Date')['Weekly_Sales'].sum().reset_index()
        line = px.line(date,x = 'Date', y = 'Weekly_Sales',title = 'Sum of Weekly Sales for selected Year', width = 1000,height=600)
        st.plotly_chart(line)

        st.markdown(f"## :rainbow[IsHoliday and Month vs Sales for selected Year]")
        data = df[df['year'] == radio]
        data['IsHoliday'] = data['IsHoliday'].map({0:'False',1:'True'})
        date = data.groupby(['month','IsHoliday'])['Weekly_Sales'].sum().reset_index()
        # st.dataframe(date)
        bar = px.bar(date, x = 'IsHoliday', y = 'Weekly_Sales', color = 'month',width = 1000)
        st.plotly_chart(bar)

        st.markdown(f"## :rainbow[IsHoliday vs Sales and Markdown for selected Year]")
        data = df[df['year'] == radio]
        data['IsHoliday'] = data['IsHoliday'].map({0:'False',1:'True'})
        date = data.groupby(['month','IsHoliday','Markdown'])['Weekly_Sales'].sum().reset_index()
        # st.dataframe(date)
        bar = px.bar(date, x = 'IsHoliday', y = ['Weekly_Sales','Markdown'],width = 1000)
        st.plotly_chart(bar)

    elif choice == 'Explore of Markdown':
        st.markdown("## :rainbow[Stores and their sum of Markdown]")
        sales = df.groupby(['Store'])['Markdown'].sum().reset_index()#.sort_values('Weekly_Sales',ascending=False).head(10)
        # st.dataframe(sales)
        st.bar_chart(sales, x = 'Store', y = 'Markdown')

        st.markdown("## :rainbow[Top 10 Store has Highest Markdown]")
        highest_sale = df.groupby(['Store'])['Markdown'].sum().reset_index().sort_values('Markdown',ascending=False).head(10)
        st.bar_chart(highest_sale, x = 'Store', y = 'Markdown', color = '#04f')

        st.markdown("## :rainbow[Top 10 Store has Lowest Markdown]")
        lowest_sale = df.groupby(['Store'])['Markdown'].sum().reset_index().sort_values('Markdown',ascending=True).head(10)
        st.bar_chart(lowest_sale, x = 'Store', y = 'Markdown',color = '#fd0')


        st.markdown("## :rainbow[Department and their sum of Markdown]")
        sales = df.groupby(['Dept'])['Markdown','Store'].sum().reset_index()#.sort_values('Weekly_Sales',ascending=False).head(10)
        # st.dataframe(highest_sale)
        st.bar_chart(sales, x = 'Dept', y = 'Markdown')

        st.markdown("## :rainbow[Top 10 Department has Highest Markdown]")
        highest_sale = df.groupby(['Dept'])['Markdown'].sum().reset_index().sort_values('Markdown',ascending=False).head(10)
        st.bar_chart(highest_sale, x = 'Dept', y = 'Markdown', color = '#3F00FF')

        st.markdown("## :rainbow[Top 10 Department has Lowest Markdown]")
        lowest_sale = df.groupby(['Dept'])['Markdown'].sum().reset_index().sort_values('Markdown',ascending=True).head(10)
        st.bar_chart(lowest_sale, x = 'Dept', y = 'Markdown', color = '#CCCCFF')

        st.markdown("## :rainbow[Sum of Markdown with their year]")
        total_year = df.groupby('year')['Markdown'].sum().reset_index()
        # st.dataframe(total_year)
        pie = px.pie(total_year, values = 'Markdown',names = 'year',width=900,height=500)
        st.plotly_chart(pie)

        col,col1 = st.columns([2,2])
        with col:    
            radio = st.radio('**Select a Year to Analyze with that year**', options = df['year'].unique(), horizontal = True)
        with col1:
            select = st.selectbox("**Select any feature**", (['Temperature','Fuel_Price','CPI','Unemployment']))       
        

        st.markdown(f"## :rainbow[{select} vs Markdown]")
        data = df[df['year'] == radio]
        dataframe = data.groupby(select)['Markdown'].sum().reset_index()
        hist = px.histogram(dataframe, x = select,y = 'Markdown', width = 1050)
        st.plotly_chart(hist)

        date = st.selectbox("**Select a feature to explore periodic wise**", (['month','day','day_of_week','year_of_week']))

        st.markdown(f"## :rainbow[{date} vs Markdown]")
        df['year_of_week'] = df1['year_of_week']
        df['day_of_week'] = df['day_of_week'].map({0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'saturday',6:'Sunday'})
        data = df[df['year'] == radio]
        dataframe = data.groupby(date)['Markdown'].sum().reset_index()
        st.bar_chart(dataframe, x = date,y = 'Markdown')

        st.markdown(f"## :rainbow[Date vs Markdown]")
        data = df[df['year'] == radio]
        date = data.groupby('Date')['Markdown'].sum().reset_index()
        line = px.line(date,x = 'Date', y = 'Markdown',title = 'Sum of Markdown for selected Year', width = 1000,height=600)
        st.plotly_chart(line)

        st.markdown(f"## :rainbow[IsHoliday and Month vs Markdown for selected Year]")
        data = df[df['year'] == radio]
        data['IsHoliday'] = data['IsHoliday'].map({0:'False',1:'True'})
        date = data.groupby(['month','IsHoliday'])['Markdown'].sum().reset_index()
        # st.dataframe(date)
        bar = px.bar(date, x = 'IsHoliday', y = 'Markdown', color = 'month',width = 1000)
        st.plotly_chart(bar)

        st.markdown(f"## :rainbow[IsHoliday vs Sales and Markdown for selected Year]")
        data = df[df['year'] == radio]
        data['IsHoliday'] = data['IsHoliday'].map({0:'False',1:'True'})
        date = data.groupby(['month','IsHoliday','Markdown'])['Weekly_Sales'].sum().reset_index()
        # st.dataframe(date)
        bar = px.bar(date, x = 'IsHoliday', y = ['Weekly_Sales','Markdown'],width = 1000)
        st.plotly_chart(bar)