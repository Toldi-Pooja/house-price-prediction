from flask import Flask, render_template, jsonify, request
import pandas as pd
import pickle
import os
from pathlib import Path

# Get absolute paths (THIS IS CRUCIAL)
backend_dir = Path(__file__).parent.absolute()
project_root = backend_dir.parent.absolute()

app = Flask(__name__,
            template_folder=str(project_root / 'frontend' / 'templates'),
            static_folder=str(project_root / 'frontend' / 'static'))

# Debug print paths (you can remove later)
print(f"✅ Project root: {project_root}")
print(f"✅ Template folder: {app.template_folder}")
print(f"✅ Static folder: {app.static_folder}")

# Load model
model_path = project_root / 'house_price_model.pkl'
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully")
except Exception as e:
    print(f"❌ Model loading failed: {str(e)}")
    exit(1)

@app.route('/')
def home():
    """Main page with form"""
    # Verify template exists
    template_path = os.path.join(app.template_folder, 'index.html')
    if not os.path.exists(template_path):
        print(f"❌ CRITICAL: Missing template at {template_path}")
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        input_data = pd.DataFrame([[
            int(data['qual']), 
            float(data['area']), 
            int(data['beds']), 
            float(data['baths']), 
            int(data['year']),
            int(data['garage']),  # New feature
            int(data['neighborhood'])  # New feature
        ]], columns=['OverallQual', 'GrLivArea', 'BedroomAbvGr', 
                    'FullBath', 'YearBuilt', 'GarageCars', 'Neighborhood'])
        
        price = model.predict(input_data)[0]
        return jsonify({'price': round(float(price), 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)