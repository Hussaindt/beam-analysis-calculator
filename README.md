# Beam Analysis Calculator

A web application to predict the elastic modulus and load at first crack for concrete beams.

## Features
- Predicts Elastic Modulus (E)
- Calculates Load at First Crack
- Calculates Deflection
- Interactive Web Interface

## Deployment Instructions (Render.com)

1. Create a free account on [Render.com](https://render.com)

2. Click "New +" and select "Web Service"

3. Connect your GitHub repository

4. Fill in the deployment details:
   - Name: beam-analysis-calculator
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

5. Click "Create Web Service"

The application will be automatically deployed and available at your Render URL.

## Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open http://localhost:5000 in your browser

## Tech Stack
- Flask
- Python
- scikit-learn
- Bootstrap
- JavaScript 