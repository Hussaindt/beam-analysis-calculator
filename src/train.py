import os
from preprocessing import load_data, prepare_features, split_and_scale_data
from model import ElasticModulusPredictor
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Create models directory if it doesn't exist
    if not os.path.exists('models'):
        os.makedirs('models')
    
    # Load and prepare data
    print("Loading and preparing data...")
    df = load_data()
    X, y = prepare_features(df)
    
    # Split and scale data
    print("Splitting and scaling data...")
    X_train, X_test, y_train, y_test, scaler = split_and_scale_data(X, y)
    
    # Initialize and train model
    print("Training model...")
    model = ElasticModulusPredictor()
    model.train(X_train, y_train)
    
    # Evaluate model
    print("Evaluating model...")
    metrics = model.evaluate(X_test, y_test)
    print("\nModel Performance:")
    print(f"RMSE: {metrics['RMSE']:.2f} N/mm²")
    print(f"R² Score: {metrics['R2']:.4f}")
    
    # Get feature importance
    feature_importance = model.get_feature_importance()
    feature_names = X.columns
    
    # Plot feature importance
    plt.figure(figsize=(10, 6))
    sns.barplot(x=feature_importance, y=feature_names)
    plt.title('Feature Importance')
    plt.xlabel('Importance Score')
    plt.tight_layout()
    plt.savefig('models/feature_importance.png')
    
    # Save the model
    print("\nSaving model...")
    model.save_model()
    print("Model saved successfully!")

if __name__ == "__main__":
    main() 