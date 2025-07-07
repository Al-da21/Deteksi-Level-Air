💧 Water Level Detection in Storage Tanks
📌 Overview
This system is designed to detect water levels in storage tanks using computer vision. It classifies the water condition into four categories: Full, Half, Low, and Empty. Built with YOLOv8, the model is capable of detecting water levels from images or video frames. A simple web-based interface using Flask allows users to upload media and view detection results directly.

🛠️ Background
Monitoring water levels in tanks is essential for resource management, especially in areas like agriculture, manufacturing, and household use. Traditional methods often rely on manual checks or sensor-based systems, which can be costly or error-prone. By applying object detection with computer vision, this system provides a scalable, accurate, and automated alternative to water level monitoring.

Water level categories:

🟩 Full → Tank is fully filled

🟨 Half → Tank is about halfway filled

🟧 Low → Water is below optimal level

🟥 Empty → Tank is empty or nearly empty


🎯 Objectives
🔍 To implement a YOLOv8 model that detects and classifies water levels in storage tanks.
🧪 To provide a proof-of-concept system for real-time tank monitoring using computer vision.

🌟 Benefits
✅ Automates water level monitoring
✅ Reduces reliance on physical or sensor-based measurements
✅ Supports image and video input
✅ Can be adapted to IoT-based systems for real-time alerts

📊 Dataset
Source: Roboflow - Water Level

Published by: Ahmad Kurnia

Classes:

full

half

low

empty

⚙️ Input & Output Support
✅ Input Formats:

Images: .jpg, .jpeg, .png

Videos: .mp4, .avi, .mov

📸 Output:

Annotated images/videos with bounding boxes and class labels

Summary of water level classification per media.


🖼️ Example


![image](https://github.com/user-attachments/assets/399ab8a7-dfe8-431e-ba51-9e3e0c63927d)


💻 Technologies Used
Python 3.x

YOLOv8 by Ultralytics

Flask

OpenCV

HTML/CSS (for basic UI)

🤝 Contributors
This repository is maintained by @aldakkk.
