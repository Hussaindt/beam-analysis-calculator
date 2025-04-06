import numpy as np
import pandas as pd
from src.model import ElasticModulusPredictor
from src.preprocessing import load_data, prepare_features, split_and_scale_data

def predict_elastic_modulus(concrete_mix, breadth, depth, length):
    """
    Predict the elastic modulus for a given beam configuration.
    
    Parameters:
    -----------
    concrete_mix : float
        Concrete mix strength in N/mm²
    breadth : float
        Beam breadth in mm
    depth : float
        Beam depth in mm
    length : float
        Beam length in mm
        
    Returns:
    --------
    float
        Predicted elastic modulus in N/mm²
    """
    # Load the original data to get the scaler
    df = load_data()
    X, y = prepare_features(df)
    _, _, _, _, scaler = split_and_scale_data(X, y)
    
    # Calculate additional features
    cross_sectional_area = breadth * depth
    moment_of_inertia = (breadth * depth**3) / 12
    
    # Create feature array
    features = np.array([[
        concrete_mix, breadth, depth, length,
        cross_sectional_area, moment_of_inertia
    ]])
    
    # Scale features
    features_scaled = scaler.transform(features)
    
    # Load the trained model
    model = ElasticModulusPredictor()
    model.load_model()
    
    # Make prediction
    prediction = model.predict(features_scaled)[0]
    
    return prediction

def main():
    # Example usage
    print("Elastic Modulus Prediction Tool")
    print("===============================")
    
    # Get input from user
    concrete_mix = float(input("Enter concrete mix strength (N/mm²): "))
    breadth = float(input("Enter beam breadth (mm): "))
    depth = float(input("Enter beam depth (mm): "))
    length = float(input("Enter beam length (mm): "))
    
    # Make prediction
    predicted_E = predict_elastic_modulus(concrete_mix, breadth, depth, length)
    
    print("\nResults:")
    print(f"Predicted Elastic Modulus: {predicted_E:.2f} N/mm²")

if __name__ == "__main__":
    main() 