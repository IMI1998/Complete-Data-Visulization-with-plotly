import plotly.graph_objects as go 
import plotly.express as px
import streamlit as st
df_cnt = px.data.gapminder()
df_us = px.data.gapminder().query("country == 'United States'")
df_tips = px.data.tips()
df = px.data.gapminder().query("continent == 'Europe' and year== 2007 and pop > 2.e6")

def bar():
    with st.expander("bar chart"):
         bar= px.bar(df_us , x='year' , y='pop')
         st.plotly_chart(bar)

    with st.expander("stack chart"):  
         stack=px.bar(df_tips , x='day' , y='tip' , color='sex',
         title='Tips by Sex on Each Day' , labels={'tip': 'Tip Amount' , 'day': 'Day of the week'}
         )  
         st.plotly_chart(stack) 

    with st.expander("Secend bar chart"):  
        bar2 = px.bar(df_tips , x='sex' , y='total_bill' , color='smoker' , barmode='group') 
        st.plotly_chart(bar2) 

    with st.expander("Custome bar chart"):

        Cbar = px.bar(df , y='pop' , x='country' , text='pop' , color='country' )  
        Cbar.update_traces(texttemplate= '%{text:.2s}', textposition='outside')
        Cbar.update_layout(uniformtext_minsize=8)
        Cbar.update_layout(xaxis_tickangle=-45)  
        st.plotly_chart(Cbar)

    with st.expander("Animated bar chart"):
          bar3 = px.bar(df_cnt , x='continent' , y='pop' , color='continent' ,
          animation_frame='year' , animation_group="country" , range_y=[0,4000000000]
          )
          st.plotly_chart(bar3)

