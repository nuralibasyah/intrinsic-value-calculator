# Value Investing – Fair Value Calculator


This repository provides a **beginner-friendly and transparent** way to estimate the intrinsic value of a stock using Python.


The goal is not to give buy/sell recommendations, but to help understand *how valuation works*.


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]
(https://colab.research.google.com/github/nuralibasyah/intrinsic-value-calculator/blob/main/notebooks/Copy%20to%20Colab%20-%20Fair%20Value%20Calculator.ipynb)


---


## ✨ Features


- Intrinsic value estimation using:
- Discounted Cash Flow (DCF)
- PER multiple
- Graham Number
- Market price fetched via `yfinance`
- Margin of Safety (MoS) calculation
- Beginner-friendly Google Colab notebook


---


## 🚀 Quick Start (No Python Installation)


You can run this project directly in **Google Colab**:


1. Open `notebooks/00_quick_start_colab.ipynb`
2. Click **Open in Colab**
3. Upload your fundamental CSV (see template below)
4. Run all cells


The notebook will:
- calculate fair value using 3 methods
- fetch the latest market price
- compute margin of safety
- export results to CSV


---


## 📊 Fundamental Data Format


Use the provided template:



Required columns:
- ticker
- year
- revenue
- net_income
- free_cash_flow
- eps
- book_value_per_share
- total_debt
- cash_and_equivalents
- shares_outstanding
- roe
- roic


---


## 🧠 Methodology Overview


- **DCF**: Estimates value based on future cash flows
- **PER**: Relative valuation using earnings
- **Graham Number**: Classical value investing metric


Final fair value is a weighted average of the three methods.


---


## ⚠️ Disclaimer


This project is for **educational purposes only**.
It is not financial advice.


---


## 🤝 Support (Optional)


If this project is useful, you may find optional support links in the README.
They are entirely voluntary.


---


## 📬 Feedback


Issues, discussions, and suggestions are very welcome.