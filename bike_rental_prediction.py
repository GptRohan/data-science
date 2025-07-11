import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Load dataset
df = pd.read_csv("bike_rentals.csv")

# Convert date
df['datetime'] = pd.to_datetime(df['datetime'])
df['hour'] = df['datetime'].dt.hour

# Features
X = df[['temp', 'humidity', 'windspeed', 'hour']]
y = df['count']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("✅ R² Score:", r2_score(y_test, y_pred))
print("📉 MSE:", mean_squared_error(y_test, y_pred))

# Plot
plt.scatter(y_test, y_pred, alpha=0.4, color='green')
plt.title("📈 Actual vs Predicted Bike Rentals")
plt.xlabel("Actual Count")
plt.ylabel("Predicted Count")
plt.show()
