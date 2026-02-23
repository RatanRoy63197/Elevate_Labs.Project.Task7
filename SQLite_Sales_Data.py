import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect Database
conn = sqlite3.connect(r"C:\Users\Xervice5433\Desktop\Ratan\sales_data.db")
cursor = conn.cursor()

# 2. Create Table (FIXED)
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales_data (
    order_id TEXT PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# 3. Insert Data (Correct executemany usage)
cursor.execute("SELECT COUNT(*) FROM sales_data")
count = cursor.fetchone()[0]

if count == 0:
    sales_data = [
        ("order1", "Saree", 287, 299),
        ("order2", "Kurta", 42, 386),
        ("order3", "Top", 268, 139),
        ("order4", "Ethnic Dress", 486, 290),
        ("order5", "Western Dress", 322, 377),
        ("order6", "Top", 123, 208),
        ("order7", "Saree", 72, 396),
        ("order8", "Kurta", 405, 88),
        ("order9", "Kurta", 232, 55),
        ("order10", "Saree", 172, 469),
        ("order11", "Western Dress", 51, 102),
        ("order12", "Ethnic Dress", 176, 167),
        ("order13", "Top", 335, 204),
        ("order14", "Ethnic Dress", 354, 150),
        ("order15", "Saree", 292, 403),
        ("order16", "Western Dress", 475, 67),
        ("order17", "Kurta", 462, 103),
        ("order18", "Top", 79, 444),
        ("order19", "Saree", 490, 340),
        ("order20", "Western Dress", 356, 267)
    ]

    cursor.executemany(
        "INSERT INTO sales_data (order_id, product, quantity, price) VALUES (?, ?, ?, ?)",
        sales_data
    )

    conn.commit()

# 4. Run Query
query = """
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales_data
GROUP BY product
"""

df = pd.read_sql_query(query, conn)

print("\nSales Summary:\n")
print(df)

# 5. Plot
df.plot(kind='bar', x='product', y='revenue')
plt.title("Revenue by Product")
plt.tight_layout()
plt.show()

conn.close()