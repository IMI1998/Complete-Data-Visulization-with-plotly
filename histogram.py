import plotly.graph_objects as go 
import plotly.express as px
import streamlit as st
import numpy as np

dice_1 = np.random.randint(1,7,5000)
dice_2 = np.random.randint(1,7,5000)
df_tips = px.data.tips()
dice_sum = dice_1 + dice_2

def histogram():
    with st.expander("Histogram chart"):
        fig = px.histogram(dice_sum , nbins=11,
                            labels={'value':'Dice Roll'},
                            title='500 Dice Roll Histogram',
                            marginal='violin',
                            color_discrete_sequence=['#F8F7F3']                  
        )
        fig.update_layout(
            xaxis_title_text='Dice Roll',
            yaxis_title_text='Dice',
             showlegend=False
        )
        st.plotly_chart(fig)

    with st.expander("2 Histogram chart together"):
         df_tips = px.data.tips()
         fig2=px.histogram(df_tips , x='total_bill' , color='sex' , color_discrete_sequence=['#fc4a1a' , '#f6b733'])
        
         st.plotly_chart(fig2)    
    with st.expander("Sub Histogram chart "):
         df_tips = px.data.tips()
         fig2=px.histogram(df_tips , x='total_bill',y='tip' , color='sex' , facet_row="time" , facet_col="day", category_orders={"day":["Thur" , "Fri" , "Sat" , "Sun"],
         "time":["Lunch" , "Dinner"]
         } )
        
         st.plotly_chart(fig2)    