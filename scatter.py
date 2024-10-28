import plotly.graph_objects as go 
import plotly.express as px
import streamlit as st
import numpy as np
import seaborn as sns

df_tips = px.data.tips()
df_iris = px.data.iris()
df_cnt = px.data.gapminder()
flights = sns.load_dataset("flights")
df = px.data.gapminder().query("year == 2007")

def scatter():

    with st.expander("Scatter plot"):
         s1 = px.scatter(df_iris , x='sepal_width' , y='sepal_length' , color='species' , size='petal_length' , hover_data=['petal_width']) 
         st.plotly_chart(s1)

    with st.expander("Secend Scatter plot"):
         fig = go.Figure()
         fig.add_trace(go.Scatter(
            x=df_iris.sepal_width , y=df_iris.sepal_length, mode='markers',
            marker_color = df_iris.sepal_width,
            text=df_iris.species, marker=dict(showscale=True , colorscale='Plasma')))
         fig.update_traces(marker_line_width=2 , marker_size=10 , )
         st.plotly_chart(fig)   

    with st.expander("Scatter plot for big data"):
         fig2 = go.Figure(data=go.Scattergl(
          x = np.random.randn(100000),
          y = np.random.randn(100000),
          mode='markers',
          marker=dict(
               color=np.random.randn(100000),
               colorscale='Plasma',
               line_width=1
               )))
         st.plotly_chart(fig2)     

    with st.expander("3DScatter plot "):  

          fig3=px.scatter_3d(flights , x='year' , y='month' , z='passengers', 
          color='year' , opacity=0.7)  
          st.plotly_chart(fig3)  

    with st.expander("Scatter Matrix plot "):
          fig4 = px.scatter_matrix(flights , color='month')  
          st.plotly_chart(fig4) 
    
    
    with st.expander(" Map Scatter plot "):
          fig5 = px.scatter_geo(df , locations="iso_alpha", 
          color="continent",
          hover_name="country",
          size="pop",
          projection="orthographic"
          )
          st.plotly_chart(fig5) 
    with st.expander(" sub Scatter plots "):
          fig6 = px.scatter(df_tips , x="total_bill" , y="tip" , color="smoker",
           facet_col="sex") 
          st.plotly_chart(fig6) 
    with st.expander(" Animated Scatter plot "):
          fig7 = px.scatter(df_cnt , x="gdpPercap" , y="lifeExp" , animation_frame='year',
           animation_group="country", size="pop" , color='continent' , hover_name="country",
           log_x=True , size_max=55 , range_x=[100 , 100000],
           range_y=[25,90]
           ) 
          st.plotly_chart(fig7) 