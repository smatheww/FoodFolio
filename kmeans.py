import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib  # To save the model and scaler

def load_data(filepath):
    """Load data from a CSV file."""
    data = pd.read_csv(filepath)
    return data

def prepare_data(data):
    """Prepares data for clustering by scaling the nutritional features."""
    scaler = StandardScaler()
    features = ['protein', 'carbs', 'fat', 'totalCalories']
    data[features] = scaler.fit_transform(data[features])
    return data, scaler  # Return data and scaler

def train_model(data, n_clusters=5):
    """Train a k-means clustering model."""
    model = KMeans(n_clusters=n_clusters, random_state=42)
    model.fit(data[['protein', 'carbs', 'fat', 'totalCalories']])
    return model

def save_model_and_scaler(model, scaler, model_filename, scaler_filename):
    """Save the trained model and scaler to files."""
    joblib.dump(model, model_filename)
    joblib.dump(scaler, scaler_filename)
    print(f"Model saved to {model_filename}")
    print(f"Scaler saved to {scaler_filename}")

def main():
    data_path = 'processedDiet.csv'
    model_path = 'kmeans_model.pkl'
    scaler_path = 'scaler.pkl'

    # Load data
    data = load_data(data_path)

    # Prepare data and get scaler
    data, scaler = prepare_data(data)

    # Train the model
    model = train_model(data)

    # Save the model and scaler
    save_model_and_scaler(model, scaler, model_path, scaler_path)

if __name__ == '__main__':
    main()
