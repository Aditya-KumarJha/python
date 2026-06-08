import streamlit as st
import pandas as pd 
import numpy as np 

## Title of the application
st.title("Hello Streamlit World! :wave:")

## Display a Simple Text
st.write("This is a simple text")

## Create a Sample DataFrame
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

## Display the DataFrame
st.write("Here is a sample DataFrame:")
st.write(df)

## Create a Line Chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.write("Here is a line chart:")
st.line_chart(chart_data)
