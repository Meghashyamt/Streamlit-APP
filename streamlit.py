import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title="Iris Data Visualization")

# Load the Iris dataset
iris_df = sns.load_dataset('iris')

# Define the layout of the app
st.title("Iris Data Visualization")
st.write("This app displays some visualizations of the Iris dataset.")

# Display the dataset
st.subheader("Iris Dataset")
st.write(iris_df)

# Create a scatter plot
st.subheader("Scatter Plot")
sns.set_style("darkgrid")
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris_df)
st.pyplot()

# Create a histogram
st.subheader("Histogram")
sns.histplot(x="petal_length", hue="species", data=iris_df, kde=True)
st.pyplot()

# Create a boxplot
st.subheader("Box Plot")
sns.boxplot(x="species", y="petal_width", data=iris_df)
st.pyplot()

# Create a pairplot
st.subheader("Pair Plot")
sns.pairplot(data=iris_df, hue="species")
st.pyplot()
