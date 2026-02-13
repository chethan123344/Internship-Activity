import matplotlib.pyplot as plt


categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
revenue = [1000, 1500, 1300, 1700, 2000]

# Create first subplot (1 row, 2 columns, position 1)
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# Create second subplot (1 row, 2 columns, position 2)
plt.subplot(1, 2, 2)
plt.plot(months, revenue)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")


plt.tight_layout()


plt.show()
