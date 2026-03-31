# DSA 210: Introduction to Data Science - Term Project
**Term:** 2025-2026 Spring
**Student:** Emre Pamukçu 
**Student ID:** 32693  

---

## Project Proposal: Impact of Fuel Prices and Holidays on Flight Ticket Pricing

### Motivation and Problem Statement
Flight ticket prices are notoriously volatile, often changing based on demand and operational costs. This project aims to analyze the relationship between ticket prices and two major external factors: global fuel prices and national holidays. By integrating these datasets, I intend to build a machine learning model that predicts ticket prices more accurately than models using only flight-specific data.

### Data Collection Strategy & Enrichment
As per the course guidelines, I am enriching a publicly available dataset with two additional data sources to provide a more comprehensive analysis.

* **Primary Dataset:** [Flight Price Prediction Dataset](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction) sourced from Kaggle. It includes features like airline, source/destination, duration, and ticket price.
* **Enrichment Data 1 (Economic):** **Historical Crude Oil (WTI) Prices** from [Oil prices dataset](https://www.investing.com/commodities/crude-oil-historical-data). This will be used to see how fluctuations in fuel costs correlate with ticket price changes.
* **Enrichment Data 2 (Seasonal):** **National Public Holidays** list from [National Holidays](https://www.kaggle.com/code/fridrichmrtn/worldwide-holiday-patterns-2024/input). This will help identify if price surges during holidays are statistically significant across different airlines.

### Data Characteristics
* **Sample Size:** Approximately 300,000 flight records.
* **Format:** All datasets will be processed and merged in `.csv` format using Python (Pandas).
* **Key Features:** Airline, Flight Duration, Departure/Arrival Time, Stops, Daily Oil Price (Enriched), and Holiday Status (Enriched).

### Planned Methodology
1.  **EDA (Exploratory Data Analysis):** Visualizing price trends in relation to oil price spikes and holiday seasons. 
2.  **Hypothesis Testing:** Testing the hypothesis: *"Do fuel price increases reflect on ticket prices immediately, or is there a time lag?"* and *"Are holiday prices significantly higher than the monthly average?"*
3.  **Machine Learning:** Implementing a **Random Forest Regressor** to predict prices. I will also perform feature importance analysis to see if "Fuel Price" is a stronger predictor than "Number of Stops."
