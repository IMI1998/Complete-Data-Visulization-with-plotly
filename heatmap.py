import plotly.graph_objects as go 
import plotly.express as px
import streamlit as st
import numpy as np
import seaborn as sns

flights = sns.load_dataset("flights")

def heatmap():
    with st.expander("Heatmap chart"):
         fig = px.density_heatmap(flights , x='year' , y='month', z='passengers' ,
         color_continuous_scale='Viridis')
         st.plotly_chart(fig)


    with st.expander("Custom Heatmap chart"):
        fig2 = px.density_heatmap(flights , x='year' , y='month', z='passengers' ,
        marginal_x='histogram',
        marginal_y='histogram'
        )
        st.plotly_chart(fig2)     