# placement-predictor
🎓 Student Placement Predictor

A web application built with Streamlit and Logistic Regression to predict whether a student will be placed in campus recruitment based on their academic performance and experience.

📌 Project Overview

This project takes student attributes such as:

College_ID

IQ

Prev_Sem_Result

CGPA

Academic_Performance

Internship_Experience

Extra_Curricular_Score

Communication_Skills

Projects_Completed

and predicts the independent variable:

Placement (Yes/No)

Currently, the model uses IQ, CGPA, and Internship_Experience as predictive features.

⚙️ Tech Stack

Python 3

Streamlit → for interactive UI

Pandas → data handling

Scikit-learn → ML model (Logistic Regression, preprocessing, train/test split)

NumPy → numerical operations

🚀 Features

✅ Uploads and processes student dataset
✅ Trains a Logistic Regression model on placement data
✅ Takes student details as input from sidebar (IQ, CGPA, Internship)
✅ Predicts placement outcome (High chance / Low chance)
✅ Displays confidence percentage
✅ Option to view the raw dataset used for training

📂 Dataset

The dataset used:
college_student_placement_dataset.csv
Contains attributes related to students’ academics, skills, and placements.

▶️ How to Run
1. Clone the repository
git clone https://github.com/your-username/student-placement-predictor.git
cd student-placement-predictor

2. Install dependencies
pip install -r requirements.txt


(requirements.txt example)

streamlit
pandas
scikit-learn
numpy

3. Run the Streamlit app
streamlit run app.py

🖼️ Example UI

Sidebar for input: IQ, CGPA, Internship Experience

Main section: Prediction result + confidence score

Option to display dataset

🔮 Future Enhancements

Include more features (Communication Skills, Projects, Extra-Curriculars, etc.)

Try different ML models (Random Forest, XGBoost, SVM)

Deploy on Streamlit Cloud / Heroku / AWS

👨‍💻 Author

Made with ❤️ by [Your Name]
