import matplotlib.pyplot as plt

# Sample country population data (in millions)
country_data = {
    "India": 1400,
    "China": 1420,
    "USA": 331,
    "Indonesia": 273,
    "Brazil": 213,
    "Nigeria": 206,
    "Pakistan": 225,
    "Bangladesh": 166
}

# Prepare data for plotting
countries = list(country_data.keys())
populations = list(country_data.values())

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(populations, labels=countries, autopct='%1.1f%%', startangle=140)
plt.title(" Population Distribution by Country")
plt.axis('equal')  # Ensures pie chart is circular
plt.tight_layout()
plt.show()
