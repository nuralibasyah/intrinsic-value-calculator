# Value Investing – Fair Value Calculator


This repository provides a **beginner-friendly and transparent** way to estimate the intrinsic value of a stock using Python.


The goal is not to give buy/sell recommendations, but to help understand *how valuation works*.


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nuralibasyah/intrinsic-value-calculator/blob/main/notebooks/Copy%20to%20Colab%20-%20Fair%20Value%20Calculator.ipynb)

[![Ko-fi](https://img.shields.io/badge/Support-Ko--fi-red?logo=ko-fi&logoColor=white)](https://ko-fi.com/nuralibasyah)
[![Saweria](https://img.shields.io/badge/Donate-Saweria-orange)](https://saweria.co/nuralibasyah)


---


## Features


- Intrinsic and fair value estimation using:
  1. Discounted Cash Flow (DCF)
  2. Graham Number
  3. PER multiple
  4. PBV multiple
  5. Combined methods with weights
- Market price fetched via `yfinance`
- Margin of Safety (MoS) calculation

---


## Quick Start (No Python Installation)


You can run this project directly in **Google Colab**:


1. Click **Open in Colab** button: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nuralibasyah/intrinsic-value-calculator/blob/main/notebooks/Copy%20to%20Colab%20-%20Fair%20Value%20Calculator.ipynb) and copy to your google account.
2. Inside the notebook, you will be prompted to upload your fundamental CSV. Use the template.csv as a template and you can add your own data.
3. Run all cells.


The notebook will:
- calculate fair value using 3 methods
- fetch the latest market price
- compute margin of safety
- export results to CSV


---


## Fundamental Data Format


Use the provided template.csv in this repo:



Required columns:
- ticker
- free_cash_flow (ttm)
- eps (ttm)
- book_value_per_share
- shares_outstanding


---


## ⚠️ Disclaimer


This project is for **educational purposes only**.
It is not financial advice.


---


## Support (Optional)


If you find this project useful, I really appreciate your support via these links:

[![Ko-fi](https://img.shields.io/badge/Support-Ko--fi-red?logo=ko-fi&logoColor=white)](https://ko-fi.com/nuralibasyah)
[![Saweria](https://img.shields.io/badge/Donate-Saweria-orange)](https://saweria.co/nuralibasyah)


---


## Feedback


Issues, discussions, and suggestions are very welcome.