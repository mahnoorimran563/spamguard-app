# 📧 SpamGuard

![Flask](https://img.shields.io/badge/Flask-2.3+-blue?logo=flask)
![Python](https://img.shields.io/badge/Made%20with-Python%203.x-yellow?logo=python)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange?logo=scikit-learn)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

**SpamGuard** is a Flask-based web application that classifies emails as **Spam** or **Ham (Not Spam)** using a trained machine learning model. It also performs **phishing keyword analysis** to enhance prediction reliability.

<br>

## 🚀 Features

- 🔍 Email classification (Spam vs Ham)
- 🧠 ML-powered prediction using Scikit-learn
- 🔐 Phishing keyword detector
- 🌐 Clean, responsive UI with HTML/CSS
- 🧪 Lightweight, fast, and secure

<br>

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask
- **ML**: Scikit-learn, Natural Language Toolkit (NLTK)
- **Deployment**: Flask built-in server (or deploy to Heroku, Render, etc.)

<br>

## 🧪 Model Training Steps

1. **Dataset**: Used the mail_data.csv
2. **Text Cleaning**:
   - Lowercasing
   - Removing stopwords and punctuation
   - Tokenization and stemming using `nltk`
3. **Feature Extraction**: TF-IDF vectorizer
4. **Model**: Multinomial Naive Bayes classifier from `sklearn`
5. **Evaluation**: Achieved ~98% accuracy on test data
6. **Exported Model**: Saved using `joblib` to `model/spam_classifier.pkl`

> For reproducibility, see `train_model.py`.

<br>

## 🖥️ Preview - Example Predictions

### 🛑 Spam Mail Detected
![Spam Example](static/assets/spam.png)

### ✅ Ham Mail Detected
![Ham Example](static/assets/ham.png)

<br>

## 📂 Project Structure

spamguard-app/
├── static/
│   └── assets/
│       └── image1.webp
├── templates/
│   ├── index.html
│   ├── result.html
├── model/
│   └── spam\_classifier.pkl
├── train\_model.py
├── app.py
├── requirements.txt
└── README.md


<br>

## 🧪 Run Locally

1. **Clone the repo**
   
   git clone https://github.com/mahnoorimran563/spamguard-app.git
   cd spamguard-app

2. **Create virtual environment (optional but recommended)**

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate


3. **Install dependencies**

   pip install -r requirements.txt


4. **Run the Flask app**

   python app.py
   

6. **Open in browser**

   http://localhost:5000


<br>

## 🔒 License

This project is licensed under the [MIT License](LICENSE).

<br>

## 🙋‍♀️ Author

**Mahnoor Imran**
💼 [LinkedIn](https://www.linkedin.com/in/mahnoorimran563)
📧 [mahnoorimran563@gmail.com](mailto:mahnoorimran563@gmail.com)

---

**Made with 💻 and ☕ by Mahnoor**

