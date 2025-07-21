from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load model & vectorizer
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def is_phishing_like(text):
    phishing_keywords = ['http', 'verify', 'account', 'bank', 'click here', 'suspend', 'login', 'password', 'urgent', 'security']
    return any(word in text.lower() for word in phishing_keywords)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ''
    if request.method == 'POST':
        email_text = request.form['email_content']
        data = vectorizer.transform([email_text])
        
        result = model.predict(data)[0]
        proba = model.predict_proba(data)[0]  # Get probabilities for both classes
        confidence = round(max(proba) * 100, 2)  # e.g., 92.47

        if is_phishing_like(email_text) and result == 1:
            result = 0
            confidence = 99.0  # Override with high confidence for phishing

        prediction = 'Ham Mail' if result == 1 else 'Spam Mail'
        prediction += f" ({confidence}% confidence)"

        
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
