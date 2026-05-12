# DSA 210: Introduction to Data Science - Term Project
**Term:** 2025-2026 Spring
**Student:** Emre Pamukçu 
**Student ID:** 22596  

---

## Final Project: Impact of Fuel Prices and Holidays on Flight Ticket Pricing

### Motivation and Problem Statement
Flight ticket prices are notoriously volatile, often changing based on demand and operational costs. The initial goal of this project was to analyze the relationship between ticket prices and two major external factors: global fuel prices (Crude Oil) and national holidays. By integrating these datasets, the project sought to build a machine learning model that predicts ticket prices and evaluates whether external factors are as important as internal flight logistics (like duration or cabin class).

### Data Collection & Enrichment
The core of this project was a publicly available dataset, enriched with two additional data sources for a more comprehensive analysis:

* **Primary Dataset:** [Flight Price Prediction Dataset](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction) sourced from Kaggle (~300,000 records). Features included airline, duration, stops, class, and ticket price.
* **Enrichment Data 1 (Economic):** **Historical Crude Oil (WTI) Prices** from [Investing.com](https://www.investing.com/commodities/crude-oil-historical-data). Used to correlate daily fuel costs with ticket price adjustments.
* **Enrichment Data 2 (Seasonal):** **National Public Holidays** list from Kaggle. Used to analyze if holiday demand surges translate to statistically significant price hikes.

### Exploratory Data Analysis & Hypothesis Testing Findings
- **Oil Prices:** Contrary to the hypothesis that rising oil prices cause immediate ticket price hikes, Pearson correlation testing (r = -0.6519) showed a negative relationship over the timeframe studied. Tests for 7-day and 14-day lag periods revealed varying correlations, highlighting the complexity and lag in airline pricing strategies.
- **Holidays:** Welch's t-test confirmed a significant difference in pricing during holidays. However, surprisingly, the mean ticket price on holidays (19,506 INR) was *lower* than non-holidays (20,946 INR). This was likely driven by a drop in expensive business-class travel during public holidays offsetting leisure travel surges.

### Machine Learning Results
A machine learning pipeline was established using scikit-learn to predict ticket prices:
1.  **Linear Regression (Baseline):** Achieved an R² Score of 0.9049 and an RMSE of 6,995 INR.
2.  **Random Forest Regressor:** After hyperparameter tuning via GridSearchCV (`n_estimators=100`, `max_depth=15`), the ensemble model achieved an R² Score of 0.9493 and an RMSE of 5,110 INR, successfully capturing non-linear relationships.

**Feature Importance Conclusion:**
The Random Forest's feature importance metric directly answered the project's core question. Internal flight characteristics—specifically **Cabin Class** (Economy vs Business) and **Flight Duration**—completely dominated the pricing model. External factors like Daily Oil Price and Holiday Status provided minimal predictive power compared to basic flight logistics.

### Methods & Tools Used
- **Data Manipulation & Cleaning:** `pandas`, `numpy` (Handling missing values, date parsing, merging datasets)
- **Statistical Analysis:** `scipy.stats` (Pearson correlation, Welch's t-test)
- **Data Visualization:** `matplotlib.pyplot`, `seaborn` (Scatter plots, boxplots, feature importance bar charts)
- **Machine Learning:** `scikit-learn`
  - `LinearRegression` for baseline modeling
  - `RandomForestRegressor` for ensemble modeling
  - `GridSearchCV` for hyperparameter tuning
  - `StandardScaler` for feature scaling
  - `pd.get_dummies` for one-hot encoding categorical variables

### Deliverables
- `eda_and_hypothesis_testing.ipynb`: Notebook detailing the EDA, visual trends, and statistical tests.
- `machine_learning_phase4.ipynb`: Notebook detailing data preprocessing, model training, and feature importance analysis.
- `Final_Report.pdf`: Comprehensive report covering the methodologies and results.
- `Final_Presentation.pptx`: Slide deck summarizing the project flow and conclusions (redesigned for presentations).
