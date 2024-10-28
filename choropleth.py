from urllib.request import urlopen
import json
import streamlit as st
import plotly.graph_objects as go 
import plotly.express as px
import pandas as pd

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)


df=pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
    dtype={"fips":str})

def choropleth ():

    with st.expander("Choropleth chart"):
        fig=px.choropleth(df , geojson=counties , locations='fips' , color='unemp',
        color_continuous_scale="Plasma",
        scope='usa',
        labels={'unemp' : 'unemployment rate'}
        )
        st.plotly_chart(fig)