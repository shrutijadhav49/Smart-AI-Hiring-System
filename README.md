# 💼 Smart AI Hiring System

### Machine Learning-Based Interview Selection Predictor

## 📌 Project Overview

The **Smart AI Hiring System** is a machine learning project developed using Python and Streamlit to predict interview selection outcomes based on candidate details and assessment scores.

The application allows users to enter candidate information, including age, gender, education, years of experience, previous companies, skill score, interview score, and personality score. A trained Random Forest model processes these inputs and predicts the hiring outcome.

The project demonstrates how machine learning can be integrated into an interactive web application for exploring candidate assessment data and predictive analytics.

## 🎯 Project Objectives

- Develop a machine learning-based interview selection prediction application.
- Analyze candidate information and assessment scores.
- Build an interactive interface using Streamlit.
- Integrate a trained Random Forest model for predictions.
- Demonstrate the practical application of Python and machine learning.

## 🖥️ Application Preview

The application provides a simple interface where users can enter candidate details and assessment scores before generating a prediction.

### Candidate Details

The application collects the following inputs:

- Age
- Gender
- Education Level
- Experience Years
- Previous Companies
- Skill Score
- Interview Score
- Personality Score

Users can adjust the input values and click **Predict Hiring Decision** to view the model's prediction.

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development and model integration |
| Streamlit | Interactive web application interface |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations and model input preparation |
| Scikit-learn | Machine learning model development and prediction |
| Random Forest | Candidate selection prediction model |
| Jupyter Notebook | Model development and experimentation |

## 📊 Machine Learning Approach

The project uses a Random Forest classifier to predict candidate selection outcomes.

### Input Features

The model receives eight candidate-related features:

1. Age
2. Gender
3. Education Level
4. Experience Years
5. Previous Companies
6. Skill Score
7. Interview Score
8. Personality Score

Categorical inputs such as gender and education level are converted into numerical values before being passed to the model.

### Prediction Process

1. The user enters candidate information.
2. The application converts categorical inputs into numerical representations.
3. The input values are prepared in the format required by the trained model.
4. The Random Forest model generates a prediction.
5. The application displays the predicted hiring outcome.

The application currently displays one of two outcomes: **Selected for Hiring** or **Not Selected**.

## 📁 Project Structure

```text
Smart_Interview_Performance/
│
├── App.py
├── Smart_Interview_Performance.ipynb
├── Smart_Interview_Performance_Dataset.csv
├── model_rf.pkl
├── requirements.txt
└── README.md
```

### File Description

- `App.py` — Streamlit application interface and prediction logic.
- `Smart_Interview_Performance.ipynb` — Jupyter Notebook for model development and experimentation.
- `Smart_Interview_Performance_Dataset.csv` — Dataset used for the project.
- `model_rf.pkl` — Saved machine learning model.
- `requirements.txt` — Python package dependencies.
- `README.md` — Project documentation.

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart_Interview_Performance.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### Step 2: Navigate to the Project Folder

```bash
cd Smart_Interview_Performance
```

### Step 3: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python -m streamlit run App.py
```

Streamlit will provide a local URL where you can open the application in your browser.

## 📈 Expected Output

After entering the candidate details and clicking the prediction button, the application displays the model's predicted outcome:

- **Selected for Hiring** — The model returns the selection class.
- **Not Selected** — The model returns the non-selection class.

These are model-generated predictions, not guaranteed hiring decisions.

## 💡 Skills Demonstrated

- Python programming
- Machine learning model integration
- Random Forest classification
- Data preparation and numerical encoding
- Streamlit application development
- Interactive input handling
- Predictive analytics
- Project documentation

## 🔮 Future Improvements

- Display model confidence or prediction probabilities where appropriate.
- Add model evaluation metrics such as accuracy, precision, recall, and F1-score.
- Improve input validation and error handling.
- Add visualizations to explore candidate assessment data.
- Document the dataset source and training methodology.
- Evaluate model fairness across candidate groups.
- Include clear limitations and human-review safeguards for hiring-related predictions.

## ⚠️ Important Disclaimer

This project is intended for educational and demonstration purposes. Its predictions should not be used as the sole basis for real recruitment decisions.

Hiring outcomes can be affected by many factors that may not be represented in the dataset. The model should be evaluated for accuracy, reliability, and potential bias before any real-world use. Human judgment and fair recruitment practices remain essential.

## 👩‍💻 Author

**Shruti Jadhav**

Data Analytics & Business Intelligence | Python | SQL | Power BI | Machine Learning

- **LinkedIn:** https://www.linkedin.com/in/shruti-jadhav-b981a7308/
- **GitHub:** https://github.com/shrutijadhav49

---

⭐ If you find this project interesting, feel free to explore the code and share your feedback.
