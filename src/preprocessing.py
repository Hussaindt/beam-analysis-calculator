import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path='data/cleaned_data.csv'):
    """Load and prepare the dataset."""
    # Read the data
    df = pd.read_csv(file_path)
    
    # Drop the unnamed index column if it exists
    if 'Unnamed: 0' in df.columns:
        df = df.drop('Unnamed: 0', axis=1)
    
    # Rename columns for clarity
    df.columns = ['concrete_mix', 'breadth', 'depth', 'length', 'elastic_modulus']
    
    return df

def prepare_features(df):
    """Prepare features for modeling."""
    # Calculate additional features that might be useful
    df['cross_sectional_area'] = df['breadth'] * df['depth']
    df['moment_of_inertia'] = (df['breadth'] * df['depth']**3) / 12
    
    # Select features for modeling
    feature_columns = [
        'concrete_mix', 'breadth', 'depth', 'length',
        'cross_sectional_area', 'moment_of_inertia'
    ]
    
    X = df[feature_columns]
    y = df['elastic_modulus']
    
    return X, y

def split_and_scale_data(X, y, test_size=0.2, random_state=42):
    """Split the data and scale the features."""
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler 