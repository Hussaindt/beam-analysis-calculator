import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

class ElasticModulusPredictor:
    def __init__(self):
        self.model = RandomForestRegressor(
            n_estimators=100,
            max_depth=None,
            min_samples_split=2,
            min_samples_leaf=1,
            random_state=42
        )
        self.scaler = None
        
    def train(self, X_train, y_train):
        """Train the model."""
        self.model.fit(X_train, y_train)
        
    def predict(self, X):
        """Make predictions."""
        return self.model.predict(X)
    
    def evaluate(self, X_test, y_test):
        """Evaluate the model performance."""
        y_pred = self.predict(X_test)
        
        # Calculate metrics
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        
        return {
            'RMSE': rmse,
            'R2': r2
        }
    
    def save_model(self, model_path='models/elastic_modulus_model.joblib'):
        """Save the trained model."""
        joblib.dump(self.model, model_path)
    
    def load_model(self, model_path='models/elastic_modulus_model.joblib'):
        """Load a trained model."""
        self.model = joblib.load(model_path)
        
    def get_feature_importance(self):
        """Get feature importance scores."""
        feature_importance = self.model.feature_importances_
        return feature_importance 