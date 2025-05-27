Scuccessfully Redicted mobile price with 89% accuracy

# Predict Mobile Phone Pricing
🔹 Step 1: Data Understanding
Already done. We have:
•	2000 rows × 21 columns
•	Target: price_range (multi-class: 0, 1, 2, 3)
•	Features: numeric + binary (e.g., ram, battery_power, touch_screen, etc.)

🔹 Step 2: Exploratory Data Analysis (EDA)
Perform:
•	Descriptive statistics (df.describe())
•	Value counts for price_range
•	Correlation matrix
•	Histograms and boxplots for feature distributions
•	Pairplots for selected features (like ram, battery_power, px_height, etc.)
👉 Helps identify outliers, skewed distributions, and top correlated features.
🔹 Step 3: Data Preprocessing
3.1. Feature Scaling
Use StandardScaler or MinMaxScaler since many models (like KNN, SVM) are sensitive to scale.
3.2. No Missing Data
Already verified: no missing/null values.
🔹 Step 4: Model Selection
Try these models:
•	Random Forest: interpretable, fast, accurate
•	Logistic Regression (multi-class)
•	XGBoost or LightGBM
•	(Optional) Neural Network
Let’s start with Random Forest Classifier.

🔹 Step 5: Model Training
🔹 Step 6: Model Evaluation and plot with ConfusionMatrix
Metrics to watch:
•	Accuracy
•	Precision / Recall / F1-score for each class (0, 1, 2, 3)
🔹 Step 7: Feature Importance
👉 This helps identify which features most affect the price prediction (typically ram, battery_power, px_width, px_height, etc.)
🔹 Step 8: Hyperparameter Tuning (Optional)
Use GridSearchCV or RandomizedSearchCV on the Random Forest or other models to fine-tune accuracy.
🔹 Step 9: Final Model & Save
🔹 Step 10: Inference and Create a Flask API
Then Deploy the model in GitHub
