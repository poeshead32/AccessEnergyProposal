import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Title of the app
st.title('Access Energy - Phase 1 Proposal for Hutton Court')

# Introduction text
st.write("This interactive proposal covers Phase 1 of the energy optimization project for Hutton Court, focusing on a 550kWh battery backup installation. Adjust the settings below to see how different backup sizes impact various metrics.")

# Dropdown for backup size options
backup_sizes = [450, 500, 550, 600, 650]
selected_size = st.selectbox('Select Backup Size (kWh)', backup_sizes)

# Generate some sample data for demonstration
# In real application, this would be replaced with actual data
def generate_data(backup_size):
    data = {
        'Time': pd.date_range(start='2023-01-01', periods=24, freq='H'),
        'Energy Usage (kWh)': np.random.normal(loc=backup_size * 0.8, scale=20, size=24),
        'Energy Saved (kWh)': np.random.normal(loc=backup_size * 0.4, scale=10, size=24),
        'Cost Savings ($)': np.random.normal(loc=backup_size * 0.5, scale=5, size=24)
    }
    return pd.DataFrame(data)

data = generate_data(selected_size)

# Function to create Altair chart
def create_altair_chart(data, y_axis_title):
    chart = alt.Chart(data).mark_line().encode(
        x='Time',
        y=alt.Y(y_axis_title, axis=alt.Axis(title=y_axis_title)),
        tooltip=[y_axis_title, 'Time']
    ).interactive().properties(
        width=700,
        height=400
    )
    return chart

# Displaying different metrics in Altair charts
st.subheader('Hourly Energy Usage (kWh)')
st.altair_chart(create_altair_chart(data, 'Energy Usage (kWh)'))

st.subheader('Hourly Energy Saved (kWh)')
st.altair_chart(create_altair_chart(data, 'Energy Saved (kWh)'))

st.subheader('Hourly Cost Savings ($)')
st.altair_chart(create_altair_chart(data, 'Cost Savings ($)'))
