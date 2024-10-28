import plotly.graph_objects as go 
import plotly.express as px
import streamlit as st
import numpy as np

df_wind = px.data.wind()


def polar():
    with st.expander("Polar chart"):
         fig = px.scatter_polar(df_wind , r="frequency" , theta="direction" , 
         color = 'strength' , size="frequency" , symbol="strength" , template="plotly_dark"
         )
         st.plotly_chart(fig)
    with st.expander("Secend Polar chart"):
         fig2 = px.line_polar(df_wind , r="frequency" , theta="direction" , 
         color = 'strength' , line_close=True , template="plotly_dark"
         )
         st.plotly_chart(fig2)