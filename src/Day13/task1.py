import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("housing_data.csv")


# Histogram with KDE
plt.subplot(1, 2,1)
sns.histplot(df["Price"], kde=True)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")


# Skewness & Kurtosis
print("Skewness:", df["Price"].skew())
print("Kurtosis:", df["Price"].kurt())


# Count Plot
plt.subplot(1, 2,2)
sns.countplot(x=df["City"])
plt.title("City Distribution")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()