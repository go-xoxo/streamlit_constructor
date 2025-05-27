import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

# 🧠 Efficiently cache the data to avoid reloading on reruns
@st.cache_data
def load_data(path):
    return pd.read_csv(path)

# 📦 Load and duplicate the raw dataset to work with a clean copy
mpg_df_raw = load_data(path="./data/mpg.csv")
mpg_df = deepcopy(mpg_df_raw)

# 🏁 Main title and header
st.title("Introduction to Streamlit")
st.header("MPG Data Exploration")

# 📋 Optional raw data display
if st.checkbox("Show Dataframe"):
    st.subheader("This is my dataset")
    st.dataframe(data=mpg_df)

# 🎛️ Three-column layout for controls
left_column, middle_column, right_column = st.columns([3, 1, 1])

# 📆 Year selection dropdown
years = ["All"] + sorted(pd.unique(mpg_df["year"]))
year = left_column.selectbox("Choose a year", years)

# 🔍 Filter dataset by year
if year == "All":
    reduced_df = mpg_df
else:
    reduced_df = mpg_df[mpg_df["year"] == year]

# ⚙️ Radio button to toggle display of class means
show_means = middle_column.radio(label="Show Class Means", options=["Yes", "No"])

# 🧮 Group-wise mean calculation for plotting
means = reduced_df.groupby("class").mean(numeric_only=True)

# 🎨 Plotting method selection
plot_types = ["matplotlib", "plotly"]
plot_type = right_column.radio("Choose Plot Type", plot_types)

# 📊 Build Plotly figure
p_fig = px.scatter(
    reduced_df,
    x="displ",
    y="hwy",
    range_x=[1, 8],
    range_y=[10, 50],
    width=750,
    height=600,
    labels={"displ": "Displacement (Liters)", "hwy": "MPG"},
    title="Engine Size vs Highway Fuel Mileage"
)

# 🔴 Optionally overlay means on Plotly plot
if show_means == "Yes":
    p_fig.add_trace(go.Scatter(x=means["displ"], y=means["hwy"], mode="markers"))
    p_fig.update_layout(showlegend=False)

# 🧰 Create Matplotlib version of the same plot
m_fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(reduced_df["displ"], reduced_df["hwy"], alpha=0.7)
ax.set_title("Engine Size vs Highway Fuel Mileage")
ax.set_xlabel("Displacement (Liters)")
ax.set_ylabel("MPG")

# 🔴 Overlay class means in red if selected
if show_means == "Yes":
    ax.scatter(means["displ"], means["hwy"], alpha=0.7, color="red", label="Class Means")

# 🎛️ Display chosen chart type
if plot_type == "matplotlib":
    st.pyplot(m_fig)
else:
    st.plotly_chart(p_fig)

# 🔗 Data source citation
url = "https://archive.ics.uci.edu/ml/datasets/auto+mpg"
st.write("Data Source", url)

# 🗺️ BONUS: quick map visual using sample data
st.subheader("Streamlit Map")
ds_geo = px.data.carshare()
ds_geo["lat"] = ds_geo["centroid_lat"]
ds_geo["lon"] = ds_geo["centroid_lon"]

# 🧾 Show sample of geographic data
st.dataframe(ds_geo.head())

# 🗺️ Plot map from lat/lon
st.map(ds_geo)
