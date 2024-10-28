import plotly.graph_objects as go 
import plotly.express as px
import streamlit as st
import numpy as np

df_asia = px.data.gapminder().query("year == 2007").query("continent == 'Asia'")


def Pi():

    with st.expander("Pie chart"):
        pi = px.pie(df_asia , values='pop' , names='country' , title='Population of Asia Continent' ,
        color_discrete_sequence=px.colors.sequential.RdBu,
        )
        st.plotly_chart(pi)

    with st.expander(" Custome Pie chart"):
        colors = ['blue' , 'green' , 'black' , 'purple' , 'red' , 'brown']
        fig = go.Figure(data=[go.Pie(labels=['Water' , 'Grass' , 'Normal' , 'Psychic' , 'Fire' , 'Ground'],
        values=[110 , 90 ,80 ,30 ,20 , 200]
        )])  

        fig.update_traces(hoverinfo='label+percent' , textfont_size=20 , textinfo='label+percent',
        pull=[0.1 , 0 , 0.2 , 0,0,0],
        marker=dict(colors=colors , line=dict(color='#FFFFFF',
        width=0.5
        ))
        )  
        st.plotly_chart(fig)
