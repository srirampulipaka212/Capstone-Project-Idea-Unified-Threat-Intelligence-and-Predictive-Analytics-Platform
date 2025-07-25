import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv('processed/cleaned_data.csv')
# Example features: event_count, threat_score, is_weekend, etc.
X = df[['event_count', 'threat_score', 'is_weekend']]
y = df['is_incident']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)
joblib.dump(model, 'models/threat_model.pkl')
