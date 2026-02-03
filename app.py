import streamlit as st 
import pickle
import numpy as np
import sys
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="Traffic Behaviour Analysis",
    page_icon="🚦",
    layout="wide",
)
st.markdown("""
# 🚦 Traffic Behavior Analysis
**Highway Traffic Insights using Computer Vision & Multi-Object Tracking**

This dashboard visualizes detection, tracking, trajectory analysis, and
statistical behavior modeling on a fixed highway traffic video.
""")

st.sidebar.header("Controls")
st.sidebar.write("Adjust analysis parameters ")
threshold_factor=st.sidebar.slider(
    "Slow vehicle threshold factor",
    min_value=0.5,
    max_value=1.0,
    value=0.8,
    step=0.05
)
with open("outputs/trajectory_data.pkl", "rb") as f:
    data = pickle.load(f)
track_history = data["track_history"]
vehicle_speeds = data["vehicle_speeds"]
fps = data["fps"]

mean_speed=np.mean(list(vehicle_speeds.values()))
std_speed = np.std(list(vehicle_speeds.values()))
slow_threshold=mean_speed-threshold_factor*std_speed
slow_vehicles = [
    vid for vid, speed in vehicle_speeds.items()
    if speed < slow_threshold
]
st.subheader("📊 Results Summary (This Video)")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Vehicles (this video)",
        value=len(vehicle_speeds)
    )

with col2:
    st.metric(
        label="Average Speed (px/sec)",
        value=round(mean_speed, 2)
    )

with col3:
    st.metric(
        label="Slow Vehicles (this video)",
        value=len(slow_vehicles)
    )
st.divider()
st.sidebar.markdown("""
**What does this control do?**

This factor determines how strictly a vehicle is classified as *slow*.
A vehicle is marked slow if its speed is significantly lower than the
average traffic speed, based on statistical deviation.

- Lower value → more vehicles classified as slow  
- Higher value → stricter definition of slow
""")

# Prepare trajectory data for plotting
trajectory_paths = []

for track_id, points in track_history.items():
    if len(points) > 20:  # ignore very short tracks
        xs, ys = zip(*points)
        trajectory_paths.append((xs, ys))
st.subheader("📈 Analysis Visualizations",divider=True)
left_vis, right_vis = st.columns([1, 1])

with left_vis:
    st.subheader("🧭 Vehicle Trajectories")

    fig, ax = plt.subplots(figsize=(3.2, 2.4))

    for xs, ys in trajectory_paths:
        ax.plot(xs, ys, linewidth=1, alpha=0.7)

    ax.set_xlabel("X (px)")
    ax.set_ylabel("Y (px)")
    ax.set_title("Motion Paths")
    ax.invert_yaxis()

    fig.tight_layout()
    st.pyplot(fig, use_container_width=False)

with right_vis:
    st.subheader("🎥 Annotated Traffic Video")
    st.caption("▶ Play to view detection and tracking results")

    st.video(r"C:\Users\vpokh\Downloads\fixed.mp4")
