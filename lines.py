import plotly.graph_objects as go 
import plotly.express as px
import streamlit as st
import seaborn as sns
flights = sns.load_dataset("flights")
att_df = sns.load_dataset("attention")
def lines():
    df_stocks = px.data.stocks()

    with st.expander("google line chart"):
         
         l1=px.line(df_stocks, x='date' , y='GOOG' , labels={'x':'Date' , 'y':'Price'})
         st.plotly_chart(l1)

    with st.expander("google and apple line chart"):
         l2 = px.line(df_stocks , x='date' , y=['GOOG' , 'AAPL'] , labels={'x': 'Date' , 'y':'Price'} , title='Apple vs. Google')
         st.plotly_chart(l2)

    with st.expander("multiple line charts"):  

         fig = go.Figure()
         fig.add_trace(go.Scatter(x=df_stocks.date , y=df_stocks.AAPL , mode='lines' , name='Apple'))   
         fig.add_trace(go.Scatter(x=df_stocks.date , y=df_stocks.AMZN , mode='lines+markers' , name='Amazon'))   
         fig.add_trace(go.Scatter(x=df_stocks.date , y=df_stocks.GOOG , mode='lines+markers' , name='Google',line=dict(color='firebrick' , width=2 , dash='dashdot')))
         fig.update_layout(title='Stock Price Data 2018 - 2020 ' , xaxis_title='Price' , yaxis_title='Date')
         st.plotly_chart(fig)   

    with st.expander("full Customization line charts"): 
       
         fig.update_layout(
          xaxis=dict(
               showline=True , showgrid=False , showticklabels=True ,
               linecolor='rgb(204 , 204 , 204)', linewidth = 2 , ticks='outside' , tickfont=dict(
                    family='Arial' , size=12 , color='rgb(82,82,82)',
          ),
          ),
          yaxis=dict(
               showgrid=False , zeroline=False , showline=False ,showticklabels=False
          ),autosize=False , margin=dict(
               autoexpand=False , l=100 , r=20 , t=110
          ),  showlegend=False , 
          )
         st.plotly_chart(fig) 


    with st.expander("3D Line plot "):  

          fig2=px.line_3d(flights , x='year' , y='month' , z='passengers', 
          color='year' )  
          st.plotly_chart(fig2)  

    with st.expander("sub Line plot "):  

          fig3=px.line(att_df , x='solutions' , y='score' , facet_col="subject", 
          facet_col_wrap=5 , title="Scores Based on Attention" )  
          st.plotly_chart(fig3)  
