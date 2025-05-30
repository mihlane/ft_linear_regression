import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv('data.csv')  # Replace with your actual file path

# Display first few rows
print(df.head())

# Basic line plot (choose your columns)
plt.figure(figsize=(10, 6))
plt.plot(df['km'], df['price'])  # Replace with actual column names
plt.xlabel('km')
plt.ylabel('price')
# plt.title('Temperature Over Time')
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.tight_layout()
plt.show()
