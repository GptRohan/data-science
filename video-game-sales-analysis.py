import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("vgsales.csv")

# Preview
print(df[['Name', 'Platform', 'Year', 'Genre', 'Global_Sales']].head())

# Drop missing years
df = df.dropna(subset=['Year'])
df['Year'] = df['Year'].astype(int)

# Top 10 selling games
top_games = df.sort_values(by='Global_Sales', ascending=False).head(10)
print("🏆 Top 10 Best-Selling Games:\n", top_games[['Name', 'Global_Sales']])

# Sales over years
year_sales = df.groupby('Year')['Global_Sales'].sum()
plt.figure(figsize=(10, 5))
year_sales.plot(kind='line', marker='o', color='purple')
plt.title("📈 Global Video Game Sales Over Years")
plt.ylabel("Sales (Millions)")
plt.grid(True)
plt.show()

# Genre-wise sales
genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values()
genre_sales.plot(kind='barh', color='teal')
plt.title("🎮 Sales by Game Genre")
plt.xlabel("Global Sales (Millions)")
plt.show()
