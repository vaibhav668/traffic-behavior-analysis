🚦 Traffic Behavior Analysis using Computer Vision

An advanced computer vision project that analyzes highway traffic behavior using YOLOv8-based object detection, multi-object tracking, and trajectory-based motion analysis.
The system extracts vehicle-level insights such as speed statistics, slow-vehicle detection, and motion patterns, and visualizes the results through an interactive Streamlit dashboard.

📽️ Demo

A working demo of the Streamlit dashboard showing annotated video output, trajectory visualization, and traffic statistics.

'Annotated video with detection & tracking

'Vehicle trajectory plot

'Interactive slow-vehicle threshold control

'Real-time metric updates (based on precomputed analysis)

🧠 Problem Statement

Understanding traffic behavior from surveillance footage is essential for traffic monitoring, congestion analysis, and intelligent transportation systems.
While object detection identifies vehicles, behavioral insights require tracking, motion analysis, and statistical reasoning.

This project aims to:

'Track multiple vehicles in highway traffic videos

'Analyze their motion trajectories and speeds

'Identify anomalous behavior such as unusually slow-moving vehicles

'Present results in a clear, interpretable dashboard

🛠️ Approach & Pipeline

The system follows a multi-stage computer vision pipeline:

1.Object Detection

'Vehicles are detected using a pretrained YOLOv8 model.

2.Multi-Object Tracking

'Persistent IDs are assigned to vehicles across frames.

'Enables trajectory construction and temporal analysis.

3.Trajectory Extraction

'Vehicle centroids are stored over time.

'Trajectories represent motion paths in image coordinates.

4.Behavior Analysis

'Average speed is computed per vehicle (pixel-based).

'A statistical threshold is applied:

        slow_threshold = mean_speed − k × std_speed


'Vehicles below this threshold are classified as slow.

5.Visualization

'Annotated video with bounding boxes and tracking IDs

'Top-down trajectory plot

'Interactive dashboard using Streamlit

✨ Key Features

'🚗 YOLOv8-based vehicle detection

'🔁 Multi-object tracking with persistent IDs

'🧭 Trajectory-based motion analysis

'📊 Statistical slow-vehicle detection

'🎥 Annotated video output

'📈 Trajectory visualization

'🎛️ Interactive Streamlit dashboard

'🧪 Reproducible offline analysis

🧰 Tech Stack

'Python

'YOLOv8 (Ultralytics)

'OpenCV

'NumPy

'Matplotlib

'Streamlit

'Pickle (for intermediate data storage)

📊 Results

'Successfully tracks multiple vehicles in highway traffic footage

'Extracts meaningful motion trajectories

'Identifies slow-moving vehicles using statistical deviation

'Provides intuitive visualization of traffic behavior

⚠️ Limitations

'Speed estimation is pixel-based and not calibrated to real-world units (km/h).

'Performance may degrade under heavy occlusions or dense traffic.

'Analysis is performed offline on a fixed input video.

🚀 Future Work

'Camera calibration for real-world speed estimation

'Lane detection for lane-wise behavior analysis

'Real-time inference on live traffic feeds

'Advanced anomaly detection using learning-based methods

👨‍💻 Author

Vaibhav Pokhriyal
B.Tech CSE (AI & ML)
Interested in Computer Vision, Machine Learning, and Intelligent Systems

⭐ Acknowledgements

Ultralytics YOLOv8

OpenCV community

Streamlit
