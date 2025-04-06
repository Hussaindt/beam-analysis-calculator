from flask import Flask, render_template, request, jsonify
import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from src.predict import predict_elastic_modulus

app = Flask(__name__)
app.config['ENV'] = 'production'
app.config['DEBUG'] = False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Extract values from request
        concrete_mix = float(data['concrete_mix'])
        breadth = float(data['breadth'])
        depth = float(data['depth'])
        length = float(data['length'])
        
        # Make prediction for elastic modulus only
        predicted_E = predict_elastic_modulus(concrete_mix, breadth, depth, length)
        
        return jsonify({
            'success': True,
            'elastic_modulus': f"{predicted_E:.2f}"
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    # Get port from environment variable or use 5000 as default
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 