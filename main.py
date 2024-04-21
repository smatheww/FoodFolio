import pandas as pd
from sklearn.preprocessing import StandardScaler


# Data Preprocessing

# Load the dataset
data = pd.read_csv('All_Diets.csv')

# Remove unnecessary columns
data.drop(['Extraction_day', 'Extraction_time'], axis=1, inplace=True)

# Rename columns
data = data.rename(columns={
    'Diet_type': 'dietType',
    'Recipe_name': 'recipeName',
    'Cuisine_type': 'cuisineType',
    'Protein(g)': 'protein',
    'Carbs(g)': 'carbs',
    'Fat(g)': 'fat'
})

# Standardize Numerical Data
scaler = StandardScaler()
data[['protein', 'carbs', 'fat']] = scaler.fit_transform(data[['protein', 'carbs', 'fat']])


# Feature Engineering

# Calculate total calories
data['totalCalories'] = data['protein'] * 4 + data['carbs'] * 4 + data['fat'] * 9
# Macronutrient Ratios
data['proteinRatio'] = (data['protein'] * 4) / data['totalCalories']
data['carbRatio'] = (data['carbs'] * 4) / data['totalCalories']
data['fatRatio'] = (data['fat'] * 9) / data['totalCalories']
# Health Index
data['healthIndex'] = (data['proteinRatio'] * 0.3) + (data['carbRatio'] * 0.4) - (data['fatRatio'] * 0.3)
# High Protein
data['highProtein'] = (data['protein'] > 0.5).astype(int)  # adjusted threshold due to standardization
# Low Carb
data['lowCarb'] = (data['carbs'] < -0.5).astype(int)  # adjusted threshold due to standardization
# Low Fat
data['lowFat'] = (data['fat'] < -0.5).astype(int)  # adjusted threshold due to standardization

# Handle categorical data
data = pd.get_dummies(data, columns=['dietType', 'recipeName', 'cuisineType'])

# Option to save preprocessed data to a new CSV file
# data.to_csv('processedDiet.csv', index=False)

# Print first few rows of preprocessed data to verify
print(data.head())