import pandas as pd
from sklearn.preprocessing import StandardScaler
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def preprocess_data():
    logging.info("Starting data preprocessing...")
    data = pd.read_csv('All_Diets.csv')

    # Initial data processing
    data.drop(['Extraction_day', 'Extraction_time'], axis=1, inplace=True)
    data.rename(columns={
        'Diet_type': 'dietType',
        'Recipe_name': 'recipeName',
        'Cuisine_type': 'cuisineType',
        'Protein(g)': 'protein',
        'Carbs(g)': 'carbs',
        'Fat(g)': 'fat'
    }, inplace=True)

    # Calculate total calories and ratios
    data['totalCalories'] = data['protein'] * 4 + data['carbs'] * 4 + data['fat'] * 9
    data['proteinRatio'] = data['protein'] * 4 / data['totalCalories']
    data['carbRatio'] = data['carbs'] * 4 / data['totalCalories']
    data['fatRatio'] = data['fat'] * 9 / data['totalCalories']
    data['healthIndex'] = data['proteinRatio'] * 0.3 + data['carbRatio'] * 0.4 - data['fatRatio'] * 0.3

    # Threshold for categorization
    data['highProtein'] = (data['protein'] > 20).astype(int)
    data['lowCarb'] = (data['carbs'] < 50).astype(int)

    # Create columns for standardized values for model training
    scaler = StandardScaler()
    data[['protein_standardized', 'carbs_standardized', 'fat_standardized']] = scaler.fit_transform(data[['protein', 'carbs', 'fat']])

    # Description for display
    data['description'] = data.apply(lambda row: f"This recipe from {row['cuisineType']} cuisine is perfect for a {row['dietType']} diet. "
                                                 f"It provides {row['totalCalories']} calories with a macronutrient distribution of "
                                                 f"{row['protein']}g protein, {row['carbs']}g carbohydrates, and {row['fat']}g fat. "
                                                 f"The health index of this recipe is {row['healthIndex']:.2f}, indicating "
                                                 f"{'a balanced' if row['healthIndex'] >= 0 else 'a less balanced'} nutritional profile.", axis=1)

    # Save to CSV
    data.to_csv('processedDiet.csv', index=False)
    logging.info("Preprocessing complete and data saved.")

if __name__ == '__main__':
    preprocess_data()
