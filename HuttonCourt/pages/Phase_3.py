import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# Page title
st.title("Access Energy - Phase 2 Proposal for Hutton Court")

# Cost Comparison
st.subheader("Cost Comparison: Diesel vs. Natural Gas Generators")
cost_data = pd.DataFrame({
    'Generator Type': ['Diesel', 'Natural Gas'],
    'Operating Cost': [50000, 30000]  # Example costs
})
cost_chart = alt.Chart(cost_data).mark_bar().encode(
    x='Generator Type',
    y='Operating Cost',
    color='Generator Type'
)
st.altair_chart(cost_chart, use_container_width=True)

# Emissions Calculator
st.subheader('Emissions Calculator')
EMISSIONS_FACTOR_DIESEL = 2.68  # kg CO2 per kWh for diesel
EMISSIONS_FACTOR_GAS = 1.22    # kg CO2 per kWh for natural gas
run_time = st.slider('Average Run Time (hours per day)', 0, 24, 8)
emissions_diesel = run_time * EMISSIONS_FACTOR_DIESEL * 275
emissions_gas = run_time * EMISSIONS_FACTOR_GAS * 275
st.write(f"Daily emissions for diesel: {emissions_diesel} kg CO2")
st.write(f"Daily emissions for natural gas: {emissions_gas} kg CO2")

# Conversion Process Timeline
st.subheader("Conversion Process Timeline")
timeline_data = pd.DataFrame([
    dict(Task="Planning", Start='2023-01-01', Finish='2023-02-01'),
    dict(Task="Procurement", Start='2023-02-02', Finish='2023-03-01'),
    dict(Task="Installation", Start='2023-03-02', Finish='2023-04-01'),
    dict(Task="Testing", Start='2023-04-02', Finish='2023-05-01'),
    dict(Task="Finalization", Start='2023-05-02', Finish='2023-06-01'),
])
fig = px.timeline(timeline_data, x_start="Start", x_end="Finish", y="Task", labels={'Task': 'Milestone'})
fig.update_yaxes(autorange="reversed")  # otherwise tasks are listed from the bottom up
st.plotly_chart(fig, use_container_width=True)

# Financial Modeling Tool
st.subheader('Financial Modeling Tool')
natural_gas_price = st.number_input('Natural Gas Price (R per kWh)', value=0.05)
expected_run_time = st.number_input('Expected Run Time (hours per year)', value=2000)
financing_cost = st.number_input('Financing Cost (%)', value=5.0)
investment = 100000  # Example investment cost for conversion
annual_savings = expected_run_time * (0.15 - natural_gas_price) * 275  # Example savings calculation
payback_period = investment / annual_savings
roi = (annual_savings - (investment * (financing_cost / 100))) / investment
st.write(f"Payback Period (years): {payback_period:.2f}")
st.write(f"Return on Investment: {roi:.2%}")
