import pandas as pd
import numpy as np
import os

# Paths
BASE_DIR = r"c:\Users\emre\OneDrive\Masaüstü\CS\CS455\emre_210\DSA210_Spring_2025_2026_TermProject"
FLIGHT_DIR = os.path.join(BASE_DIR, "dataset", "flight")
OIL_FILE = os.path.join(BASE_DIR, "dataset", "oil_price_11022022_31032022", "Crude Oil WTI Futures Historical Data.csv")

print("Loading flight data...")
economy_df = pd.read_csv(os.path.join(FLIGHT_DIR, "economy.csv"))
business_df = pd.read_csv(os.path.join(FLIGHT_DIR, "business.csv"))

# Tag class
economy_df['class'] = 'Economy'
business_df['class'] = 'Business'

# Combine
flight_df = pd.concat([economy_df, business_df], ignore_index=True)

print("Cleaning flight prices and dates...")
# Price cleaning (remove commas and quotes)
flight_df['price'] = flight_df['price'].str.replace(',', '').astype(int)

# Date conversion (Flight: DD-MM-YYYY)
flight_df['date'] = pd.to_datetime(flight_df['date'], format='%d-%m-%Y')

print("Loading oil price data...")
oil_df = pd.read_csv(OIL_FILE)

# Date conversion (Oil: MM/DD/YYYY)
oil_df['date'] = pd.to_datetime(oil_df['Date'], format='%m/%d/%Y')
oil_df['oil_price_wti'] = oil_df['Price'].astype(float)

# Select relevant oil columns
oil_clean = oil_df[['date', 'oil_price_wti']]

print("Merging datasets...")
# Merge flight and oil
merged_df = flight_df.merge(oil_clean, on='date', how='left')

# Interpolate missing oil prices for weekends (if any)
merged_df['oil_price_wti'] = merged_df['oil_price_wti'].interpolate(method='linear')

print("Adding holiday flags...")
# Indian Holidays: March 1 (Maha Shivaratri), March 18 (Holi)
holiday_dates = [pd.to_datetime('2022-03-01'), pd.to_datetime('2022-03-18')]
merged_df['is_holiday'] = merged_df['date'].isin(holiday_dates)

print(f"Saving merged data (Rows: {len(merged_df)})...")
output_path = os.path.join(BASE_DIR, "master_flight_data.csv")
merged_df.to_csv(output_path, index=False)

print(f"Successfully saved to: {output_path}")
