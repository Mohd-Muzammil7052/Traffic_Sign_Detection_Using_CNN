# 🚦 Traffic Sign Detection Using CNN  

A **deep learning project** that classifies traffic signs from images using a **Convolutional Neural Network (CNN)**.  
The trained model is deployed as a **Streamlit web application**, where users can upload an image of a traffic sign and get real-time predictions.  

---

## 📑 Table of Contents  

- [📖 Introduction](#-introduction)  
- [✨ Features](#-features)  
- [📂 Dataset](#-dataset)  
- [🚀 Installation](#-installation)  
- [⚙️ Setup](#️-setup)  
- [🖥️ Usage](#️-usage)  
- [🛠️ Tech Stack](#-tech-stack)  
- [📌 Requirements](#-requirements)  
- [🏗️ Project Structure](#️-project-structure)  
- [📄 License](#-license)  
- [🤝 Contributing](#-contributing)  
- [📧 Contact](#-contact)  

---

## 📖 Introduction  

Traffic signs play a crucial role in road safety.  
This project uses a **CNN model** trained on a traffic sign dataset to recognize different traffic signs.  
The model is deployed with **Streamlit** so users can interact with it easily by uploading an image of a sign.  

---

## ✨ Features  

- 📸 **Upload an image** → Supports `.jpg`, `.jpeg`, and `.png`  
- 🔍 **CNN-powered classification** → Predicts traffic sign class with high accuracy  
- 🖼️ **Displays uploaded image** → Shows preprocessed image before prediction  
- 🚀 **Real-time prediction** → Instant classification inside browser  
- 🌐 **Streamlit UI** → User-friendly interface  

---

## 📂 Dataset  

- Dataset used: **German Traffic Sign Recognition Benchmark (GTSRB)**  
- Processed and balanced dataset is stored in:  
  - `archive_upd_bal.zip` → Contains training and testing images  
- Mapping file:  
  - `traffic_sign.csv` → Contains `ClassId` and corresponding `Name` of traffic signs  

---

## 🚀 Installation  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/Mohd-Muzammil7052/Traffic_Sign_Detection_Using_CNN.git
cd Traffic_Sign_Detection_Using_CNN
pip install -r requirements.txt
```
---

## ⚙️ Setup

1. Ensure the trained model file traffic_sign_classifier.h5 is present in the project root.

2. Keep traffic_sign.csv in the root directory for label mapping.

3. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🖥️ Usage

1. Open the app in your browser.
2. Upload an image of a traffic sign.
3. Click Predict.
4. The predicted traffic sign name will be displayed.
---

## 🛠️ Tech Stack

* Python → Core language
* TensorFlow → CNN model
* Streamlit → Web app
+ Pandas → CSV handling
* NumPy → Preprocessing
* PIL (Pillow) → Image processing

---

## 📌 Requirements

See [requirements.txt](https://github.com/Mohd-Muzammil7052/Traffic_Sign_Detection_Using_CNN/blob/main/requirements.txt) for all dependencies:

```text
tensorflow
streamlit
pandas
numpy
Pillow
```

---

## 🏗️ Project Structure  

```text
📦 Traffic-Sign-Detection-CNN
 ┣ 📜 app.py                     # Streamlit app
 ┣ 📜 model.ipynb                # Model training notebook
 ┣ 📜 traffic_sign.csv           # ClassId → Sign name mapping
 ┣ 📜 archive_upd_bal.zip        # Balanced dataset
 ┣ 📜 requirements.txt           # Dependencies
 ┣ 📜 traffic_sign_classifier.h5 # Trained CNN model (not uploaded here)
 ┗ 📜 README.md                  # Documentation
```

---

## 📄 License  

This project is licensed under the [MIT License](https://opensource.org/license/mit).  
Feel free to use, modify, and distribute it as needed.

---

## 🤝 Contributing  

Contributions are welcome! 🎉  
If you’d like to improve this project:  

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to the branch (`git push origin feature-branch`)  
5. Open a Pull Request  

---

## 📧 Contact  

For queries or collaborations:  

**Mohd Muzammil**  
- [GitHub](https://github.com/Mohd-Muzammil7052)  
- [LinkedIn](https://www.linkedin.com/in/mohd-muzammil-109044290/)

---
