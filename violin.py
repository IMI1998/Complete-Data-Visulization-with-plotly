import plotly.graph_objects as go 
import plotly.express as px
import streamlit as st
import numpy as np

df_tips = px.data.tips()

def violin():
   with st.expander("Violin chart"):
       v = px.violin(df_tips , y='total_bill' , box=True , points='all')
       st.plotly_chart(v)

   with st.expander("Secend Violin chart"):
       v1 = px.violin(df_tips , y='tip' ,x='smoker', box=True , points='all' , color='sex' , hover_data=df_tips.columns)
       st.plotly_chart(v1)  

   with st.expander("Custome Violin chart"):
        fig = go.Figure()
        fig.add_trace(go.Violin(x=df_tips['day'][df_tips['smoker']=='Yes'],
        y=df_tips['total_bill'][df_tips['smoker']=='Yes'],
        legendgroup='Yes' , scalegroup='Yes' , name='Yes',
        side='negative' , line_color='blue'
        ))      
        fig.add_trace(go.Violin(x=df_tips['day'][df_tips['smoker']=='No'],
        y=df_tips['total_bill'][df_tips['smoker']=='No'],
        legendgroup='Yes' , scalegroup='Yes' , name='No',
        side='positive' , line_color='red'
        ))   
        st.plotly_chart(fig)   