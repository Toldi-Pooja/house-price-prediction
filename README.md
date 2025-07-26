# 🏠 AI-Powered House Price Prediction

![App Demo](assets/demo.gif)  
*Live demo screenshot/GIF*

A full-stack machine learning application that predicts housing prices with **87% accuracy** (R² score) using XGBoost and Flask.

## ✨ Key Features
- **Interactive Web Interface**: User-friendly form with real-time predictions
- **Machine Learning Model**: XGBoost regression trained on 1,400+ data points
- **Responsive Design**: Works on mobile and desktop
- **API Endpoint**: `/predict` for programmatic access

## 🛠️ Tech Stack
| Component       | Technology |
|-----------------|------------|
| **Frontend**    | HTML5, CSS3, JavaScript |
| **Backend**     | Python Flask |
| **ML Model**    | XGBoost, Scikit-learn |
| **Deployment**  | Render (Free Tier) |

## 🚀 Quick Start
### Local Development
```bash
# 1. Clone repository
git clone https://github.com/yourusername/house-price-prediction.git

# 2. Install dependencies
pip install -r backend/requirements.txt

# 3. Run the application
python backend/app.py

## � Local Setup
```bash
git clone https://github.com/Toldi-Pooja/house-price-prediction.git
cd house-price-prediction
pip install -r backend/requirements.txt
python backend/app.py

📊 Performance Metrics
Metric	Value
R² Score	0.89
MAE	$12,500# Stage the untracked files
git add backend/README.md house_price_model.pkl train.csv

# Verify what will be committed
git status

# Commit the files
git commit -m "Add model, dataset, and backend README"

# Push to GitHub
git push origin main