🚗 BMW Sales Analysis (2010–2024)

This project analyzes BMW car sales from **2010 to 2024** using Python. It provides visual insights into yearly sales trends, model-wise performance, and sales distribution by fuel type.

---

📌 Features

### ✔️ Yearly Sales Analysis

Plots total BMW sales for each year using a line graph.

### ✔️ Model-wise Sales Trends

Shows how each BMW model performed from 2010–2024.

### ✔️ Total Sales Distribution (Pie Chart)

Displays how much each model contributed to the total BMW sales.

### ✔️ Fuel-Type Based Sales Analysis

Compares sales across different fuel types using a bar chart.

---

📂 Project Structure

```
Bmw.py                                # Main analysis script
BMW sales data (2010-2024).csv        # Dataset
README.md                             # Documentation (this file)
```

---

## 🛠️ Requirements

Install the required libraries:

```bash
pip install numpy pandas matplotlib
```
 ▶️ How to Run the Script

1. Place `Bmw.py` and the CSV file in the project directory.
2. Update the CSV path inside the script if needed.
3. Run the script:

```bash
python Bmw.py
```

4. Visual graphs will open automatically.

---

 📊 Functions Explained

1. **Total_sales(df, Unique_years)**

* Calculates and plots total sales per year.
* Line graph for 2010–2024.

2. **Series(df, Unique_years, model)**

* Shows year-wise contribution (%) of a selected model.
*  Creates an individual line graph for each model.

3. **total_series(df, models)**

* Computes total sales volume of each model.
* Displays a pie chart showing contribution per model.

4. **salesByFueltype(df)**

* Groups data by fuel type.
* Displays a bar graph of total sales by fuel category.

📈 Sample Visuals Generated

* 📉 Yearly sales trend
* 🧮 Percent-wise model sales
* 🥧 Total model distribution
* 📊 Fuel type comparison

---
🚀 Future Enhancements

* Convert analysis into a **Streamlit dashboard**.
* Add forecasting using **machine learning (ARIMA / LSTM)**.
* Add interactive filters for year/model/fuel type.
* Export reports as PDF.

👨‍💻 Author
Developed by Eswar Vivek.
