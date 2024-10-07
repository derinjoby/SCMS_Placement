# **Pharmacy Analysis Project**

This project involves the analysis of a dataset of pharmacies across the United States and its territories. The primary aim of the analysis is to clean the dataset, perform geospatial and statistical analysis, and visualize the results in various formats.

## **Project Structure**
This repository contains the following key components:

- `Analysis.py`: Python script that performs data cleaning, analysis, and visualization.
- `pharmacies_heatmap.html`: Heatmap showing the geographic distribution of pharmacies.
- `pharmacies_by_state.png`: Bar plot showing the number of pharmacies by state.
- `pharmacies_per_county.png`: Bar plot showing the number of pharmacies in the top 20 counties.
- `ownership_by_state.png`: Plot of pharmacy ownership type (chain vs independent) by state.
- `pharmacy_services_by_naics.png`: Bar plot showing pharmacy services based on NAICS descriptions.
- `cleaned_pharmacies.csv`: Cleaned dataset ready for further analysis.

---

## **1. Requirements**

To run the analysis script, you'll need the following Python libraries installed:

```bash
pip install pandas geopandas matplotlib seaborn folium
```

If you're using a virtual environment (venv), activate it before installing dependencies.

```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
pip install -r requirements.txt  # Ensure this file includes dependencies like pandas, geopandas, etc.
```

---

## **2. Analysis Workflow**

The script performs several types of analysis and visualization, broken down into the following sections:

### **1. Data Cleaning and Preparation**
- Loads the dataset (`Pharmacies.csv`) and drops unnecessary or empty columns.
- Cleans the dataset by removing rows with missing coordinates (`X`, `Y`) or other essential data.

### **2. Geospatial Analysis - Heatmap**
- Generates a heatmap using `folium` to show the geographic distribution of pharmacies.
- The heatmap is saved as an HTML file (`pharmacy_heatmap.html`).

### **3. Aggregation by Region**
- Aggregates the number of pharmacies by state and county, and creates bar plots to visualize the data.
- `pharmacies_by_state.png`: Number of pharmacies per state.
- `pharmacies_per_county.png`: Number of pharmacies in the top 20 counties.

### **4. Ownership Structure (Chain vs Independent)**
- Visualizes the ownership structure of pharmacies across different states using a count plot.
- The ownership structure is inferred from the `ENT_TYPE` column, and the plot is saved as `ownership_by_state.png`.

### **5. Pharmacy Services and NAICS Code Analysis**
- Analyzes the type of pharmacy services based on NAICS code descriptions (`NAICSDESCR`).
- The result is visualized in a bar plot and saved as `pharmacy_services_by_naics.png`.

### **6. Temporal Analysis (Optional)**
- Though not implemented in the final version, this section can be used to analyze pharmacy data over time using the `CONTDATE` field.

### **7. Export Cleaned Data**
- The cleaned dataset is exported to a new CSV file (`cleaned_pharmacies.csv`) for future analysis.

---

## **3. Running the Script**

1. Clone this repository.
2. Make sure you have installed all the necessary dependencies.
3. Update the `file_path` in the script to point to the location of your `Pharmacies.csv` file.
4. Run the `Analysis.py` script:

```bash
python Analysis.py
```

5. After the script is executed, you will see the following outputs:
   - `pharmacies_heatmap.html`
   - Several `.png` files for various visualizations.
   - `cleaned_pharmacies.csv` file.

---

## **4. Output Files**
- **HTML Heatmap**: Visualizes the density of pharmacies across the U.S.
- **PNG Visualizations**: Includes several bar plots for pharmacy counts by state, county, ownership, and services.
- **Cleaned Dataset**: Exported as `cleaned_pharmacies.csv`.

---

## **5. Project Notes**

- The script uses `geopandas` and `folium` for geospatial analysis, so make sure these libraries are correctly installed in your environment.
- Data cleaning focuses on ensuring that essential fields like geographic coordinates, state, and zip codes are present.
- The visualizations provide insights into the geographic and ownership distribution of pharmacies as well as the type of services they provide.

---

## **6. License**

This project is open-source and available under the MIT License.

---

## **7. Future Enhancements**
- **Temporal Analysis**: Analysis of changes over time based on the `CONTDATE` field.
- **Interactive Dashboards**: Adding dashboards to make the visualizations interactive.
- **Enhanced Geospatial Analysis**: Further exploration into regional trends using more detailed geospatial data.

---

Feel free to reach out if you have any questions or suggestions for improvements!

--- 

