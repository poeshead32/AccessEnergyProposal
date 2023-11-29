import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import altair as alt

st.title("Access Energy - Phase 2 Proposal for Hutton Court")
# Assume the coordinates for Hutton Court
HUTTON_COURT_COORDS = [28.0331, -26.1286]  # Replace with actual coordinates
MAPBOX_TOKEN = 'pk.eyJ1IjoicG9lc2hlYWQzMiIsImEiOiJjbHBqZ3E4a3gwYjVmMmlxb3cydGZ0Z3hkIn0.zsWJvBuTWotxlXiYb0cZeA'
pdk.settings.mapbox_key = MAPBOX_TOKEN
# 1. Interactive Map
st.subheader("Interactive Map of PV Installation Site")
map = pdk.Deck(
    map_style="mapbox://styles/mapbox/streets-v12",
    initial_view_state={
        "latitude": HUTTON_COURT_COORDS[1],
        "longitude": HUTTON_COURT_COORDS[0],
        "zoom": 15,
        "pitch": 50,
    },
    layers=[]
)
st.pydeck_chart(map)

# 2. Slider for PV Panel Configuration
st.subheader("PV Panel Configuration")
kw_capacity = st.slider("Select PV Capacity (kW)", 100, 300, 240)

# 3. Solar Energy Calculator
st.subheader("Solar Energy Calculator")
sun_hours = st.number_input("Average Sunny Hours per Day", value=5.0, min_value=0.0, step=0.5)
energy_output = kw_capacity * sun_hours  # Simplified calculation
st.write(f"Estimated Daily Energy Output: {energy_output} kWh")

# 4. Cost-Benefit Analysis
st.subheader("Cost-Benefit Analysis")
# Example data, replace with real data
data = pd.DataFrame({
    'Year': range(1, 11),
    'Costs': np.random.uniform(10000, 20000, 10),
    'Savings': np.random.uniform(12000, 22000, 10)
})
data['Net Savings'] = data['Savings'] - data['Costs']

# Creating the Altair chart
cost_benefit_chart = alt.Chart(data).mark_line().encode(
    x='Year:N',
    y=alt.Y('Net Savings:Q', axis=alt.Axis(title='Net Savings (R)')),
    tooltip=['Year', 'Net Savings']
)
st.altair_chart(cost_benefit_chart, use_container_width=True)

# 6. Data Tables
st.subheader("Projected Energy Production")
# Example data, replace with real data
energy_data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Projected Energy (kWh)': np.random.uniform(5000, 10000, 12)
})
st.table(energy_data)
