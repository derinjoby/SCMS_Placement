# Import necessary libraries
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Load the dataset
file_path = 'C:\\Users\\HP\\Desktop\\SCMS_Placement\\Pharmacies.csv'  # Update the file path if necessary
df = pd.read_csv(file_path)

# Inspect the data
print(df.head())
print(df.info())  # Check data types and missing values

# ====================================
# 1. Data Cleaning and Preparation
# ====================================

# Drop irrelevant or empty columns (if any are present)
df_cleaned = df.drop(columns=['ADDRESS2', 'CONTHOW', 'GEODATE', 'GEOHOW', 'HSIPTHEMES', 'PHONELOC', 'QC_QA', 'PROVID_11', 'PROVID_12', 'PROVID_20', 'PROVID_21'])

# Check for missing values
missing_values = df_cleaned.isnull().sum()
print(missing_values)

# Drop rows with missing essential data such as coordinates and state information
df_cleaned = df_cleaned.dropna(subset=['X', 'Y', 'STATE', 'ZIP'])

# Convert `X`, `Y` to float for geospatial analysis
df_cleaned['X'] = pd.to_numeric(df_cleaned['X'], errors='coerce')
df_cleaned['Y'] = pd.to_numeric(df_cleaned['Y'], errors='coerce')

# ====================================
# 2. Geospatial Analysis - Heatmap of Pharmacies
# ====================================

# Create a GeoDataFrame for geospatial analysis
gdf = gpd.GeoDataFrame(df_cleaned, geometry=gpd.points_from_xy(df_cleaned['X'], df_cleaned['Y']))

# Create a heatmap to visualize pharmacy density
pharmacy_locations = df_cleaned[['Y', 'X']].dropna()

heat_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)  # Centered on the U.S.
HeatMap(pharmacy_locations.values.tolist(), radius=10).add_to(heat_map)

# Save and display the heatmap
heat_map.save('pharmacy_heatmap.html')
heat_map  # To display in notebook

# ====================================
# 3. Aggregation by Region (State/County)
# ====================================

# Aggregating pharmacies by state
state_count = df_cleaned.groupby('STATE').size().reset_index(name='Pharmacy_Count')
print(state_count)

# Aggregating by county
county_count = df_cleaned.groupby('COUNTY').size().reset_index(name='Pharmacy_Count')
print(county_count)

# Plot the number of pharmacies by state
plt.figure(figsize=(12, 8))
sns.barplot(x='Pharmacy_Count', y='STATE', data=state_count.sort_values(by='Pharmacy_Count', ascending=False))
plt.title('Number of Pharmacies by State')
plt.xlabel('Number of Pharmacies')
plt.ylabel('State')
plt.show()

# ====================================
# 4. Ownership Structure (Chain vs Independent)
# ====================================

# Check for chain or independent pharmacies based on ORGAN_NAME or ENT_TYPE
ownership_structure = df_cleaned.groupby(['ENT_TYPE', 'STATE']).size().reset_index(name='Count')

# Plot ownership type across states
plt.figure(figsize=(14, 8))
sns.countplot(x='STATE', hue='ENT_TYPE', data=df_cleaned)
plt.title('Pharmacy Ownership Type by State')
plt.xlabel('State')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.legend(title='Ownership Type')
plt.show()

# ====================================
# 5. Pharmacy Services and NAICS Code Analysis
# ====================================

# Check NAICS code descriptions
naics_count = df_cleaned.groupby('NAICSDESCR').size().reset_index(name='Count')

# Plot pharmacy services by NAICS code
plt.figure(figsize=(12, 8))
sns.barplot(x='Count', y='NAICSDESCR', data=naics_count.sort_values(by='Count', ascending=False))
plt.title('Pharmacy Services by NAICS Description')
plt.xlabel('Number of Pharmacies')
plt.ylabel('Service Type')
plt.show()

# ====================================
# 7. Export Cleaned Data (Optional)
# ====================================

# Save the cleaned dataset to a new CSV
df_cleaned.to_csv('cleaned_pharmacies.csv', index=False)