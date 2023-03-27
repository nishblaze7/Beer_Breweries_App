import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import os
import seaborn as sns

def main():
    st.set_page_config(layout="wide")
    st.image("beers.png")

st.subheader("Information on datasets used is avaliable on the sidebar")
with st.sidebar:
  if st.checkbox("beer_reviews"):
   st.write("You have selected beer reviews, this dataset contains beer reviews from people around the United States")
  if st.checkbox("bar_location"):
   st.write("You have selected bar_location, this dataset will help you find popular breweies around you. Choose this dataset to look at the brewery map on the bottom of the page")


#Read data
df = pd.read_csv('Beer-reviews.csv')
df2 = pd.read_csv('bar_location.csv')

# show dataset
if st.checkbox("Show dataset"):
  number = st.number_input("Number of rows to view",5,100)
  st.dataframe(df.head(number))

#select columns
if st.checkbox("Select Columns to Show"):
  all_columns = df.columns.tolist()
  selected_columns = st.multiselect("Select", all_columns)
  new_df = df[selected_columns]
  st.dataframe(new_df)

#show summary
if st.checkbox("Summary"):
  st.write(df.describe().T)

#plots
st.subheader ("Data Viz")

all_columns_names = df.columns.tolist()
type_of_plot = st.selectbox("Select Type of Plot",["bar", "area", "line","hist"])
selected_columns_names = st.multiselect("Select Columns to plot", all_columns_names)

if st.button("Generate Plot"):
  st.success("Generate custom plot of {} for {}".format(type_of_plot,selected_columns_names))
  #Plot 
  if type_of_plot == 'area':
    cust_data = df[selected_columns_names]
    st.area_chart(cust_data)
elif type_of_plot == 'bar':
    cust_data = df[selected_columns_names]
    st.bar_chart(cust_data)
elif type_of_plot == 'line':
    cust_data = df[selected_columns_names]
    st.line_chart(cust_data)


if st.checkbox("Correlation Plot(Seaborn)"):
  st.write(sns.heatmap(df.corr(),annot=True))
  st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

brewery = st.selectbox('Select a brewery', df2['Brewery'])
filtered_df = df2[df2['Brewery']==brewery]
st.dataframe(filtered_df)

st.map(filtered_df)
