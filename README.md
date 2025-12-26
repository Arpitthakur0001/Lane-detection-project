# Lane Detection Project 🚗🛣️

This project performs **lane detection on road images** using a custom-trained
object detection model deployed via **Roboflow Serverless Inference**.

---

## 🔍 Project Overview
The system takes a road image as input and detects lane markings
(solid and dashed lanes). The detected lanes are visualized on the image
and the total number of detected lanes is returned.

---

## 🛠️ Tech Stack
- Python
- Roboflow Inference SDK
- Object Detection (Computer Vision)
- Serverless API Deployment

---

## ⚙️ Workflow
1. Input road image is provided
2. Image is sent to Roboflow Serverless API
3. Object detection model predicts lane markings
4. Output image is generated with detected lanes
5. Total lane count is returned

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install inference-sdk
