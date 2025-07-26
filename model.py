import pandas as pd
from xgboost import XGBRegressor
import pickle
from sklearn.model_selection import train_test_split

# Load data with MORE features
df = pd.read_csv("train.csv")[['OverallQual', 'GrLivArea', 'BedroomAbvGr', 
                             'FullBath', 'YearBuilt', 'GarageCars', 
                             'Neighborhood', 'SalePrice']]

# Convert neighborhoods to numbers
df['Neighborhood'] = df['Neighborhood'].astype('category').cat.codes

# Split data
X = df.drop('SalePrice', axis=1)
y = df['SalePrice']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train XGBoost model
model = XGBRegressor(n_estimators=1000, learning_rate=0.01)
model.fit(X_train, y_train)

# Save model
with open('house_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print(f"✅ Model trained! Score: {model.score(X_test, y_test):.2f}")