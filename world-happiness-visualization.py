import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from a public repository
data_url = "https://raw.githubusercontent.com/UBC-MDS/exploratory-data-viz/main/data/happiness.csv"
df = pd.read_csv(data_url)

# Display the structure of the dataset
print("📌 Dataset overview:")
print(df.head())

# Set up the visual style for better aesthetics
sns.set(style="whitegrid")

# Create a scatter plot to explore the correlation between GDP and happiness
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='GDP per capita',
    y='Happiness score',
    hue='Region',
    palette='Set2'
)

# Add informative labels and title
plt.title('😊 Happiness Score vs GDP per Capita by Region', fontsize=16)
plt.xlabel('GDP per Capita', fontsize=12)
plt.ylabel('Happiness Score', fontsize=12)

# Move the legend outside the plot for clarity
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the final visualization
plt.tight_layout()
plt.show()
