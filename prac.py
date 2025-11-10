import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data4 = pd.read_csv("/content/combined_dataset.csv")

st.title(" ASCII Climate Storyboard")
year = st.slider("Select Year", int(data4['year'].min()), int(data4['year'].max()), 2000)

row = data4[data4['year'] == year].iloc[0]
temp, co2 = row['temperature_celsius'], row['co2_ppm']

ice = '^' * max(1, 20 - int(temp*2))
# Sea level data is not available, represent with a placeholder
ocean = "~"*8 # Placeholder
st.text(f"Year {year}\n{ice} (ice)\n#######. (land)\n{ocean} (ocean)")

fig, ax = plt.subplots()
data4.groupby('year')['temperature_celsius'].mean().plot(ax=ax, color='tomato')
plt.title("Global Temperature Anomaly Over Time")
st.pyplot(fig)