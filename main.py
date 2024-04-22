import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('All_Diets.csv')

# Remove unnecessary columns
data.drop(['Extraction_day', 'Extraction_time'], axis=1, inplace=True)

# Rename columns to fit camel case
data = data.rename(columns={
    'Diet_type': 'dietType',
    'Recipe_name': 'recipeName',
    'Cuisine_type': 'cuisineType',
    'Protein(g)': 'protein',
    'Carbs(g)': 'carbs',
    'Fat(g)': 'fat'
})

# Feature Engineering before scaling
data['totalCalories'] = data['protein'] * 4 + data['carbs'] * 4 + data['fat'] * 9
data['proteinRatio'] = (data['protein'] * 4) / data['totalCalories']
data['carbRatio'] = (data['carbs'] * 4) / data['totalCalories']
data['fatRatio'] = (data['fat'] * 9) / data['totalCalories']
data['healthIndex'] = (data['proteinRatio'] * 0.3) + (data['carbRatio'] * 0.4) - (data['fatRatio'] * 0.3)

# Define thresholds for high protein and low carb
protein_threshold = 20  # Adjust this value based on your dietary criteria
carb_threshold = 50    # Adjust this value based on your dietary criteria

# Calculate highProtein and lowCarb before standardizing the nutritional data
data['highProtein'] = (data['protein'] > protein_threshold).astype(int)
data['lowCarb'] = (data['carbs'] < carb_threshold).astype(int)

# Standardize Numerical Data
scaler = StandardScaler()
data[['protein', 'carbs', 'fat']] = scaler.fit_transform(data[['protein', 'carbs', 'fat']])

# Categorical data handling
data = pd.get_dummies(data, columns=['dietType', 'cuisineType'])

# Save preprocessed data
data.to_csv('processedDiet.csv', index=False)

# Verify the preprocessing
print(data.head())
