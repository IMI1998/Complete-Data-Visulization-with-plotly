import plotly.graph_objects as go 
import plotly.express as px
import streamlit as st
import numpy as np

df_tips = px.data.tips()
df_stocks = px.data.stocks() 
def box():
    
    with st.expander("Box plot"):
        box = px.box(df_tips , x='sex' , y='tip' , points='all')
        st.plotly_chart(box)


    with st.expander(" Secend Box plot"):
        box2 = px.box(df_tips , x='day' , y='tip' , color='sex')
        st.plotly_chart(box2) 


         
    with st.expander(" Custom Box plot"):
         fig = go.Figure()
         fig.add_trace(go.Box(x=df_tips.sex , y =df_tips.tip,
         marker_color='blue',
         boxmean='sd',
         
         ))
         st.plotly_chart(fig)  

    with st.expander("2 Box plot together"):
          fig2 = go.Figure()
          fig2.add_trace(go.Box(y=df_stocks.GOOG , boxpoints='all' , fillcolor='blue' , jitter=0.5 , whiskerwidth=0.2))     
          fig2.add_trace(go.Box(y=df_stocks.AAPL , boxpoints='all' , fillcolor='red' , jitter=0.5 , whiskerwidth=0.2))
          fig2.update_layout(title='Google vs, Apple',
          yaxis=dict(
            # gridcolor = 'rgb(255,255,255)' ,
             gridwidth=3), 
        #   paper_bgcolor='rgb(243,243,243)',
        #   plot_bgcolor='rgb(243,243,243)'
          )     
          st.plotly_chart(fig2) 