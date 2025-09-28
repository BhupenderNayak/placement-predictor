<div align="center">

# 🎓 Student Placement Predictor 🎓

<p>
  A machine learning web application built with <strong>Streamlit</strong> and <strong>Scikit-learn</strong> to predict campus placement outcomes for students based on their academic and personal profiles.
</p>

<img src="assets/Screenshot 2025-09-28 204846.png">

</div>

---
## 🖼️ User Interface & Output Examples

## 🖼️ User Interface & Output Examples

Here are some screenshots demonstrating the application's interactive interface and prediction capabilities.

<div align="center">

### **High Chance of Placement**
<p>
  The app clearly indicates a "High Chance of Placement" when a student's profile aligns well with successful placement criteria. The confidence score provides a quantitative measure of the prediction.
</p>
<img src="assets/Screenshot 2025-09-28 204935.png" alt="High Chance Prediction" width="700">

### **Low Chance of Placement**
<p>
  Conversely, the predictor flags a "Low Chance of Placement" when input metrics suggest a lower probability, helping to identify at-risk profiles.
</p>
<img src="assets/Screenshot 2025-09-28 204904.png" alt="Low Chance Prediction" width="700">

### **Raw Dataset View**
<p>
  Users can opt to view the underlying dataset used to train the model, offering transparency and context for the predictions.
</p>
<img src="assets/Screenshot 2025-09-28 204952.png" alt="Raw Data View" width="700">

### **Logistic Regression Decision Boundary**
<p>
  A visualization from the Jupyter Notebook showing the decision boundary of the Logistic Regression model. This plot illustrates how the model separates students predicted to be placed from those who are not based on their standardized IQ and CGPA.
</p>
<img src="assets/Screenshot 2025-09-28 205035.png" alt="Decision Boundary Plot" width="700">

</div>

## 📌 Project Overview

This project implements a **Logistic Regression** model to classify whether a student is likely to be placed (`Yes`) or not (`No`) during campus recruitment. The application provides an interactive and user-friendly interface where users can input student details and receive an instant prediction along with a confidence score.

While the dataset contains numerous features, this model is currently trained on the following key predictors:
* **IQ Score**
* **CGPA**
* **Internship Experience**

---

## ✨ Features

<ul>
    <li>🚀 **Interactive UI:** Clean and simple interface built with Streamlit.</li>
    <li>🧠 **ML Model Integration:** Uses a trained Logistic Regression model from Scikit-learn.</li>
    <li>📊 **Dynamic Prediction:** Takes user inputs from a sidebar to generate real-time predictions.</li>
    <li>📈 **Confidence Score:** Displays the placement probability as a percentage.</li>
    <li>📋 **Data Display:** Includes an option to view the raw dataset used for training the model.</li>
</ul>

---

## ⚙️ Tech Stack

<p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
    <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
    <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
    <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="Numpy">
</p>

---

## 🚀 Finally starting Raje
📂 Dataset
The model is trained on the college_student_placement_dataset.csv file, which contains various attributes related to students’ academic performance, skills, and final placement status.

🔮 Future Enhancements
Potential improvements for the project include:

<ul>
<li><b>Feature Expansion:</b> Incorporate more features like Communication Skills, Projects Completed, and Extra-Curriculars to improve model accuracy.</li>
<li><b>Model Exploration:</b> Experiment with other classification models such as Random Forest, XGBoost, or Support Vector Machines (SVM).</li>
<li><b>Deployment:</b> Deploy the application to a cloud platform like Streamlit Cloud, Heroku, or AWS for public access.</li>
<li><b>Dashboarding:</b> Add a dashboard to visualize key insights from the dataset.</li>
</ul>

👨‍💻 Connect with Me
<p>
Made with ❤️ by <strong>Bhupender Nayak</strong>
</p>

<p>
<a href="https://github.com/BhupenderNayak"><img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub"></a>
<a href="https://www.linkedin.com/in/bhupendernayak"><img src="https://www.google.com/search?q=https://img.shields.io/badge/LinkedIn-0A66C2%3Fstyle%3Dfor-the-badge%26logo%3Dlinkedin%26logoColor%3Dwhite" alt="LinkedIn"></a>
</p>
