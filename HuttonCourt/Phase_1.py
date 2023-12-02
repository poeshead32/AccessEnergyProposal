import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt


st.title('Phase 1: Battery Backup Solution for Hutton Court')

#def show_outright_purchase_details():
# Function to calculate payback period (This is a simplified version, you'll need to add your actual financial calculations here)
def calculate_payback(battery_cost, annual_diesel_savings):
# Calculate payback period
    payback_period = battery_cost / annual_diesel_savings
    return payback_period


# Hardcoded values based on provided information
diesel_cost_per_liter = st.number_input("Cost of diesel per liter (Rands)", value=23)  # Cost of diesel per liter
#diesel_liters_per_kwh = st.number_input("Diesel consumed per kWh", value=0.27)  # Diesel consumed per kWh
diesel_liters_per_kwh = 0.27 # Diesel consumed per kWh
#average_daily_usage_kwh = st.number_input("Average daily usage at Hutton Court", value=1400)  # Average daily usage at Hutton Court
average_daily_usage_kwh = 1400
load_shedding_hours_per_day = st.number_input("Average load shedding hours per day", value=5)  # Average load shedding hours per day
days_per_year = 365  # Number of days in a year for load shedding


# Calculate the energy required to cover load shedding per day
energy_required_per_day = (average_daily_usage_kwh / 24) * load_shedding_hours_per_day
st.write(f"Daily power required to eliminate load-shedding: {energy_required_per_day:,.2f}kWh")
#energy_required_per_day_with_backup = ((average_daily_usage_kwh / 24) * load_shedding_hours_per_day) - 
# Calculate the total annual diesel usage for load shedding
annual_diesel_usage_liters = energy_required_per_day * diesel_liters_per_kwh * days_per_year

# Calculate the annual diesel cost for load shedding
annual_diesel_cost = annual_diesel_usage_liters * diesel_cost_per_liter

max_required_per_day = int((energy_required_per_day/5)*1.2)
# Calculate the cost of the battery backup system
# Here we determine the number of batteries needed, rounding up to the nearest whole number
#number_of_batteries = -(-energy_required_per_day // 5)  # 5kWh is the capacity of one battery, using ceiling division for rounding up
number_of_batteries = st.slider("Select the number of batteries", 0, max_required_per_day)
battery_cost = number_of_batteries * 18000  # Cost per battery
battery_capacity = number_of_batteries * 5
# Calculate the payback period
payback_period = calculate_payback(battery_cost, annual_diesel_cost)
#battery_capacity_kwh = 5  # Each battery has 5 kWh capacity
required_capacity_kwh = 300  # Required capacity to eliminate load shedding
cost_per_kwh = diesel_liters_per_kwh*diesel_cost_per_liter  # Cost per kWh from diesel generator


# Calculate fuel cost based on number of batteries
def calculate_fuel_cost(num_batteries):
    #total_backup_capacity = num_batteries * battery_capacity_kwh
    energy_shortfall = max(0, energy_required_per_day - battery_capacity)
    fuel_cost = energy_shortfall * cost_per_kwh #daily rate
    return fuel_cost

new_fuel_cost_yearly = (calculate_fuel_cost(number_of_batteries))*days_per_year
new_fuel_usage_yearly = new_fuel_cost_yearly/diesel_cost_per_liter

st.write(f"Number of 5kWh batteries required: {number_of_batteries} which will equate to {battery_capacity}kWh")
st.write(f"Estimated cost for the battery system: R{battery_cost:,.2f}")
#st.write(f"Current annual cost of diesel for load shedding: R{annual_diesel_cost:,.2f} at {annual_diesel_usage_liters:,.2f} litres")
#st.write(f"Projected annual cost of diesel for load shedding with battery system: R{new_fuel_cost_yearly:,.2f} at {new_fuel_usage_yearly:,.2f} litres")
st.write(f"Estimated payback period: {payback_period:.2f} years")

# Data for the old and new scenarios
data = pd.DataFrame({
    'Scenario': ['Current', 'With Battery System'],
    'Annual Cost': [annual_diesel_cost, new_fuel_cost_yearly],
    'Annual Litres': [annual_diesel_usage_liters, new_fuel_usage_yearly]
})

# Display the current and projected annual costs and usage
col1, col2 = st.columns(2)
with col1:
    st.header(f"*R {annual_diesel_cost:,.2f}*")
    st.write(f"Current annual cost of diesel for load shedding at {annual_diesel_usage_liters:,.0f} litres")
with col2:
    st.header(f"*R {new_fuel_cost_yearly:,.2f}*")
    st.write(f"Projected annual cost of diesel for load shedding with battery system at {new_fuel_usage_yearly:,.0f} litres")

# Create a bar chart
chart = alt.Chart(data).mark_bar().encode(
    x='Scenario:N',
    y='Annual Cost:Q',
    color='Scenario:N',
    tooltip=['Scenario:N', 'Annual Cost:Q', 'Annual Litres:Q']
).properties(
    width=600,
    height=400
)

st.altair_chart(chart, use_container_width=True)





def show_ppa_arrangement_details():
    def calculate_payback(battery_capacity, average_load_shedding_hours, cost_per_kwh, battery_cost):
        # Placeholder for the actual calculation
        # Assume a simple calculation where battery cost is divided by cost savings per year
        # You will replace this with your actual financial model
        cost_savings_per_year = battery_capacity * cost_per_kwh * average_load_shedding_hours * 365  # Example data
        payback_period = battery_cost / cost_savings_per_year  # Example data
        return payback_period

    # Assuming you have data for average load shedding hours per year
    average_load_shedding_hours = st.number_input('Average Load Shedding Hours per Year', value=4)  # Example data
    cost_per_kwh = st.number_input('Cost per kWh (R)', value=1.85)  # Actual data needed here
    battery_cost_per_kwh = st.number_input('Battery Cost per kWh (R)', value=500)  # Actual data needed here

    st.title('Phase 1: Battery Backup Solution for Hutton Court')

    # Interactive slider for selecting the battery backup size
    battery_capacity = st.slider('Select battery backup capacity (kWh)', 100, 500, 250)

    # Calculate the cost of the battery system
    battery_cost = battery_capacity * battery_cost_per_kwh  # This will change based on actual cost

    # Calculate the payback period
    payback_period = calculate_payback(battery_capacity, average_load_shedding_hours, cost_per_kwh, battery_cost)

    # Display the cost and payback period
    st.write(f"The total cost for a {battery_capacity} kWh battery system is: R{battery_cost:,.2f}")
    st.write(f"The estimated payback period is: {payback_period:.2f} years")

    # Option to choose between purchase and PPA arrangement


    # Placeholder function to calculate emissions (You will need actual emissions factors for accurate calculations)
    def calculate_emissions(diesel_usage, battery_capacity, diesel_emission_factor, grid_emission_factor):
        # Calculate current emissions from diesel usage
        current_emissions = diesel_usage * diesel_emission_factor  # Example data
        
        # Calculate reduced emissions after battery system implementation
        # Assuming battery system reduces the diesel generator usage by a significant factor
        reduced_emissions = (diesel_usage - (battery_capacity / 500 * diesel_usage)) * grid_emission_factor  # Example data
        
        return current_emissions, reduced_emissions

    # Example emission factors (You will need to replace these with actual data)
    diesel_emission_factor = 2.68  # kg CO2 per liter of diesel
    grid_emission_factor = 0.85  # kg CO2 per kWh from grid (This is an example and would be lower than diesel)

    # Assume a certain amount of diesel usage that the battery system is intended to replace (You will need actual data)
    diesel_usage = st.number_input('Monthly Diesel Usage (Liters)', value=2302)  # Actual data needed here

    # Calculate emissions with the given battery capacity
    current_emissions, reduced_emissions = calculate_emissions(diesel_usage, battery_capacity, diesel_emission_factor, grid_emission_factor)

    # Plotting the emissions comparison
    fig, ax = plt.subplots()
    bar_width = 0.35
    index = np.arange(2)
    bar1 = ax.bar(index[0], current_emissions, bar_width, label='Current Emissions')
    bar2 = ax.bar(index[1], reduced_emissions, bar_width, label='Reduced Emissions')

    ax.set_xlabel('Emission Type')
    ax.set_ylabel('Emissions (kg CO2)')
    ax.set_title('Emissions Comparison')
    ax.set_xticks(index)
    ax.set_xticklabels(['Current', 'With Battery'])
    ax.legend()

    st.pyplot(fig)

    # Display the reduction in emissions
    st.write(f"Current emissions from diesel usage: {current_emissions:,.2f} kg CO2")
    st.write(f"Reduced emissions with battery backup: {reduced_emissions:,.2f} kg CO2")
    st.write(f"Reduction in emissions: {current_emissions - reduced_emissions:,.2f} kg CO2")

    # The rest of your Streamlit app code...

    pass

# Financing option radio buttons at the top
financing_option = st.radio(
    "Select the financing option for the battery backup system:",
    ('Outright Purchase', 'PPA Arrangement')
)


    

#if financing_option == 'Outright Purchase':
 #   show_outright_purchase_details()
#else:
 #   show_ppa_arrangement_details()


