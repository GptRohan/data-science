import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("Metro_Interstate_Traffic_Volume.csv")

# Select features
df['date_time'] = pd.to_datetime(df['date_time'])
df['hour'] = df['date_time'].dt.hour

# Basic clean & select
X = df[['temp', 'rain_1h', 'snow_1h', 'clouds_all', 'hour']]
y = df['traffic_volume']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(" R² Score:", r2_score(y_test, y_pred))
print(" MSE:", mean_squared_error(y_test, y_pred))

# Plot actual vs predicted
plt.scatter(y_test, y_pred, alpha=0.3)
plt.title(" Actual vs Predicted Traffic Volume")
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.grid(True)
plt.show()
