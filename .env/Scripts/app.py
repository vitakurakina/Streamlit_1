import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image

def load_data():
    file_path = "C:/Users/talin/Desktop/osu/3k_2sem/Streamlit/Dataset/drivers.csv"
    return pd.read_csv(file_path)
df = load_data()

with st.sidebar:
    st.header("Settings")

    color = st.color_picker("Pick markdown color", "#8EE680")
    st.markdown(f"<hr style='border-color: {color}'>", unsafe_allow_html=True)

    show_cats = st.checkbox("Show cats", value=False)

    st.markdown(f"<hr style='border-color: {color}'>", unsafe_allow_html=True)

    selected_nationality = st.selectbox(
        "Pick nationality",
        options=df['nationality'].unique()
    )

st.title("Formula 1 World Championship Data - Drivers")

if show_cats:
    st.header("Cats are driving!")
    st.text("Join them!")
    img = Image.open("C:/Users/talin/Desktop/osu/3k_2sem/Streamlit/catsdriving.jpg")
    st.image(img, width=1000)

st.markdown(f"<hr style='border-color: {color}'>", unsafe_allow_html=True)
st.header("Information about Formula 1 drivers")

fig = px.histogram(df, x='nationality', title='Distribution by country',color_discrete_sequence=[color])
st.plotly_chart(fig)

sort_option = st.radio(
    "Sort:",
    options=["Driver's ID", "Name", "Birth Date"],
    horizontal=True
)

if sort_option == "Name":
    df = df.sort_values("forename")
elif sort_option == "Birth Date":
    df = df.sort_values("dob")
else:
    df = df.sort_values("driverId")

filtered_df = df[df['nationality'] == selected_nationality]

st.text(f"{selected_nationality} drivers are shown")
st.dataframe(filtered_df)

st.markdown(f"<hr style='border-color: {color}'>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total", len(df))
with col2:
    st.metric(f"From {selected_nationality}", len(filtered_df))
with col3:
    earliest_dob = filtered_df['dob'].min()
    st.metric("The oldest driver", earliest_dob)

selected_driver = st.selectbox(
    "Choose a driver for details",
    options=filtered_df['forename'].unique()
)

driver_details = filtered_df[filtered_df['forename'] == selected_driver].iloc[0]
st.json(driver_details.to_dict())
