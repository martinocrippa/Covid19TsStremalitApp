# libs
import streamlit as st
import pandas as pd

# header app
st.title('😷 Monitoring Covid19 App 🦠')
st.header('This is a sample streamlit app')

# Get data from epidemilogy data about Covid19
# More info on the data set: https://github.com/GoogleCloudPlatform/covid-19-open-data#aggregated-table
data = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', index_col='date', parse_dates=True)

# country list for options button
country = list(data['location'].unique())

# Ask the user to select a county
option = st.selectbox('Select a country:', country)

# Query the data set to get the case counts for the last 30 days for the chosen county
cases = data.loc[data['location']==option,['total_cases']].fillna(0)

# Render a line chart showing the cases
f"Daily Cases in {option}"
st.line_chart(cases)

# to execute: ...\SNOWFLAKE_material_quickstarts_handson> streamlit run .\script\Covid19_noSnowFlake_app.py
