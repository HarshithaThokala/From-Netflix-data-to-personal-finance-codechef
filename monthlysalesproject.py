import matplotlib.pyplot as plt

# Load Monthly Sales Data
def load_sales_data():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    sales = [12000, 15000, 17000, 16000, 18000, 20000,
             22000, 21000, 19000, 23000, 25000, 27000]

    return months, sales


# Visualize Sales Trend (Line Chart)
def plot_sales_trend(months, sales):
    plt.figure(figsize=(10, 6))
    plt.plot(months, sales,
             color='b',
             marker='o',
             linestyle='-',
             linewidth=2,
             label="Monthly Sales")

    plt.title("Monthly Sales Trend (2025)")
    plt.xlabel("Month")
    plt.ylabel("Sales Amount ($)")
    plt.grid(True)
    plt.legend()
    plt.savefig("sales_trend.png")


# Compare Monthly Sales (Bar Chart)
def plot_sales_bar_chart(months, sales):
    plt.figure(figsize=(10, 6))
    plt.bar(months, sales,
            color='orange',
            label="Monthly Sales")

    plt.title("Monthly Sales Comparison")
    plt.xlabel("Month")
    plt.ylabel("Sales Amount ($)")
    plt.grid(True)
    plt.legend()
    plt.savefig("sales_bar_chart.png")
