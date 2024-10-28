import plotly.graph_objects as go 
import plotly.express as px
import streamlit as st
import numpy as np

df_exp = px.data.experiment()

def ternary():

    with st.expander("Ternary chart"):

        fig= px.scatter_ternary(df_exp , a="experiment_1",
        b="experiment_2" , c="experiment_3", hover_name="group" , color="gender"
        )

        st.plotly_chart(fig)