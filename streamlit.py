import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page title
st.set_page_config(page_title="My First Streamlit App")

# Define the layout of the app
st.title("My First Streamlit App")
st.write("Welcome to my app!")

# Generate some random data
df = pd.DataFrame(np.random.randn(50, 2), columns=['x', 'y'])

# Create a scatter plot using Plotly Express
fig = px.scatter(df, x='x', y='y')

# Display the plot
st.plotly_chart(fig)
