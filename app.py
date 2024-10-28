import streamlit as st
import pandas as pd 
import numpy as np 
import chart_studio.plotly as py 
import cufflinks as cf 
import seaborn as sns 
import plotly.express as px
import matplotlib.pyplot as plt
from plotly.offline import iplot
from lines import lines
from bar import bar
from scatter import scatter
from pi import Pi
from histogram import histogram
from box import box
from violin import violin
from heatmap import heatmap
from choropleth import choropleth
from polar import polar
from ternary import ternary


arr_1 = np.random.rand(50 , 4)
df_1 = pd.DataFrame(arr_1 , columns=['A','B','C','D'])

df_cnt = px.data.gapminder()
def main():
    st.header("Complete Plotly Data visulization")
    menu = ["Home" , "Line plots" , "Bar charts" , "Scatter plots" , "Pi charts" , "Histogram charts" , "Box charts" ,
    "Violin charts" , "Heatmap charts" , "Choropleth charts" , "Polar charts" , "Ternary charts"
    ]
    choice = st.sidebar.selectbox("Menu" , menu)

    if choice =="Home":
        st.subheader("Demo")
        pl = px.line(df_1 )
        st.plotly_chart(pl)
        fig = px.line(df_cnt , x="gdpPercap" , y="lifeExp" , animation_frame='year',
           animation_group="country" , color='continent' , hover_name="country",
           log_x=True  , range_x=[100 , 100000],
           range_y=[25,90]
           ) 
        st.plotly_chart(fig) 
        
    if choice == "Line plots":
        lines()  

    if choice == "Bar charts":
        bar()

    if choice == "Scatter plots":
        scatter() 

    if choice == "Pi charts":
        Pi()  

    if choice == "Histogram charts":
        histogram()  

    if choice == "Box charts":
        box()

    if choice == "Violin charts":
        violin()  

    if choice == "Heatmap charts" :
        heatmap()  

    if choice =="Choropleth charts":
        choropleth()  

    if choice == "Polar charts":
        polar()

    if choice == "Ternary charts":
        ternary()                   
      
       
        
        




if __name__ == '__main__':
    main()

