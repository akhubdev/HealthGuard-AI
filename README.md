
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:064E3B,50:059669,100:06B6D4&height=230&section=header&text=HealthGuard%20AI&fontSize=48&fontColor=FFFFFF&fontAlignY=38&desc=Machine%20Learning%20Based%20Diabetes%20Risk%20Prediction&descAlignY=60&descSize=16&animation=fadeIn" width="100%" alt="HealthGuard AI"/>

### Healthcare Analytics & Machine Learning

![Python](https://img.shields.io/badge/Python-064E3B?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-047857?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0891B2?style=for-the-badge&logo=scikitlearn&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-0E7490?style=for-the-badge&logo=sqlite&logoColor=white)

</div>

---

## 📌 Project Overview

**HealthGuard AI** is an academic healthcare analytics project developed as part of a B.Tech final-year project.

The application uses a trained machine learning model to estimate diabetes risk from selected health indicators. It combines predictive analytics with a Flask-based web application to make model predictions accessible through an interactive interface.

The project demonstrates how machine learning, data analysis, database management, and web development can work together in a healthcare analytics use case.

## 🎯 Problem Statement

Diabetes risk assessment involves multiple health and lifestyle indicators. Analyzing these indicators can help explore patterns associated with diabetes and demonstrate how machine learning can support risk estimation.

HealthGuard AI was developed as an educational prototype to apply machine learning techniques to this problem and present the results through a web-based dashboard.

**Important:** This project is for academic and educational purposes only. It is not a medical diagnostic tool and must not be used to make healthcare decisions.

## 🎯 Project Objectives

- Build a machine learning model for diabetes risk prediction.
- Apply a trained model through a Flask web application.
- Present predictions in an accessible interface.
- Maintain prediction history using a database.
- Display healthcare analytics through a dashboard.
- Generate downloadable PDF reports.
- Demonstrate the integration of machine learning and web technologies.

## ✨ Key Features

- **Diabetes Risk Prediction:** Generate model-based risk estimates from user-provided health indicators.
- **Analytics Dashboard:** Present summary statistics and visual analytics.
- **Prediction History:** Store and review previous predictions.
- **PDF Reports:** Generate downloadable prediction reports.
- **Database Integration:** Use SQLite for application data storage.
- **User Authentication:** Provide login functionality.
- **Web Interface:** Access application features through a Flask-powered interface.
- **Cloud Deployment:** A hosted demo is available, subject to deployment availability.

## 🧠 Machine Learning Workflow

The project follows a general machine learning prediction workflow:

1. **Dataset:** Use health-indicator data for the diabetes prediction task.
2. **Data Preparation:** Prepare the selected input features for model training and prediction.
3. **Model Training:** Train a machine learning model using Python and scikit-learn.
4. **Model Persistence:** Save the trained model for later use by the application.
5. **Prediction:** Pass the submitted input features to the trained model.
6. **Web Integration:** Display the prediction through the Flask application.
7. **Record Management:** Store prediction history and support report generation.

The exact preprocessing steps, model algorithm, feature list, and evaluation results should be documented alongside the implementation and training code.

## 📊 Dataset

The project uses the **Diabetes Health Indicators dataset based on BRFSS 2015**.

Dataset file referenced in the project:

`diabetes_012_health_indicators_BRFSS2015.csv`

The dataset contains health-related indicators used to explore diabetes status and related risk factors.

The dataset is intended for statistical and machine learning analysis. Its patterns and predictions should not be interpreted as proof that an individual will or will not develop diabetes.

## 📈 Model Evaluation

Model performance should be assessed using appropriate classification metrics, such as:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

**Evaluation results:** Not included in this README because verified metric values have not yet been documented here.

Actual results should be added after checking the model-training or evaluation code. Accuracy alone may not adequately describe performance when target classes are imbalanced.

## 🖥️ Application Screenshots

Screenshots can be added here to demonstrate the implemented application.

Recommended screenshots:

- Main dashboard
- Diabetes risk prediction form
- Prediction result
- Prediction history
- PDF report preview

Store the screenshots in a repository folder such as `screenshots/` and link them here after uploading the actual image files.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application and machine learning logic |
| Flask | Web application framework |
| Scikit-learn | Machine learning |
| SQLite | Database |
| HTML | Page structure |
| CSS | Interface styling |
| JavaScript | Frontend interactions, where implemented |
| ReportLab | PDF report generation, where used |
| Render | Cloud hosting |

## 🏗️ Project Structure

The repository contains the following main components:

```text
HealthGuard-AI/
├── dataset/
├── static/
├── templates/
├── app.py
├── database.py
├── model.py
├── diabetes_model.pkl
├── requirements.txt
├── runtime.txt
└── README.md
```

- `app.py` — Flask application entry point.
- `database.py` — Database-related functionality.
- `model.py` — Model-related code.
- `diabetes_model.pkl` — Saved model artifact.
- `dataset/` — Dataset files.
- `templates/` — HTML templates.
- `static/` — Static frontend assets.
- `requirements.txt` — Python dependencies.
- `runtime.txt` — Runtime configuration.

## 🚀 Live Demo

Try the deployed application:

**[Open HealthGuard AI](https://healthguard-ai-x9xd.onrender.com)**

The demo may be unavailable during hosting maintenance or while the service is inactive.

## ⚙️ Run Locally

Username: admin Password: 1234

### Prerequisites

- Python installed
- Git installed
- A local copy of this repository

### 1. Clone the repository

```bash
git clone https://github.com/akhubdev/HealthGuard-AI.git
cd HealthGuard-AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

Open the local URL printed by Flask in your terminal, commonly `http://127.0.0.1:5000`.

**Note:** Local setup may require additional configuration depending on the database initialization, model-loading code, and environment variables used by the application.

## 🔒 Privacy & Responsible Use

- Do not submit real patients' personal or medical information to a public demo.
- Use synthetic or non-identifying data for testing.
- Do not expose production credentials or sensitive database records.
- Predictions are model estimates, not medical advice.
- Clinical use would require appropriate validation, privacy safeguards, and qualified medical oversight.

## ⚠️ Limitations

- Model predictions depend on the dataset, input features, and training process.
- Dataset patterns may not generalize to every population.
- Verified model-performance metrics must be documented before drawing conclusions about predictive quality.
- The project is an educational prototype, not a clinically validated medical system.
- Hosted application availability depends on the deployment environment.

## 🔮 Future Improvements

- Document and compare multiple classification algorithms.
- Add verified evaluation metrics and confusion-matrix visualizations.
- Improve model interpretability and feature-level explanations.
- Strengthen input validation, authentication, and security.
- Improve accessibility and responsive dashboard design.
- Add automated model evaluation and reproducible training documentation.
- Explore model monitoring and data-drift detection.

## 🎓 Academic Project

**Project:** HealthGuard AI — Diabetes Risk Prediction System  
**Domain:** Machine Learning and Healthcare Analytics  
**Academic context:** B.Tech Computer Science and Engineering final-year project

The project demonstrates the application of machine learning concepts to a healthcare-related prediction problem and integrates the trained model into a web application.

## 👨‍💻 Author

**Akash Das**

B.Tech — Computer Science and Engineering

[![GitHub](https://img.shields.io/badge/GitHub-064E3B?style=for-the-badge&logo=github&logoColor=white)](https://github.com/akhubdev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0891B2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/akashdastech)

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:064E3B,50:059669,100:06B6D4&height=160&section=footer&text=THANK%20YOU%20FOR%20VISITING!&fontSize=26&fontColor=FFFFFF&fontAlignY=65" width="100%" alt="Thank You for Visiting HealthGuard AI"/>

**Made with ❤️ by Akash Das**

</div>
