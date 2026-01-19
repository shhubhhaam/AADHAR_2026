# Aadhaar Analytics Dashboard

A comprehensive analytics dashboard for exploring Aadhaar biometric enrollment, demographic, and enrolment data in India.

## 📊 Datasets Overview

This project includes three main datasets that contain information about Aadhaar (India's biometric identity system):

### 1. **Biometric Data** (`DF_BIOMETRIC_*.csv`)
- **Description**: Contains biometric enrollment information from Aadhaar
- **Coverage**: Fingerprint, iris, and other biometric metrics across different age groups
- **Age Groups**: 5-17 years and 17+ years
- **Granularity**: National, State, and District level data
- **Files**: Split into 5 parts (`DF_BIOMETRIC_1.csv` through `DF_BIOMETRIC_5.csv`)

### 2. **Demographic Data** (`DF_DEMOGRAPHIC_*.csv`)
- **Description**: Contains demographic information of Aadhaar enrollees
- **Coverage**: Age distribution, gender, residence type, and population statistics
- **Age Groups**: 0-5 years, 5-17 years, and 18+ years
- **Granularity**: National, State, and District level data
- **Files**: Split into 5 parts (`DF_DEMOGRAPHIC_1.csv` through `DF_DEMOGRAPHIC_5.csv`)

### 3. **Enrolment Data** (`DF_ENROLMENT_*.csv`)
- **Description**: Contains Aadhaar enrolment volume and trends over time
- **Coverage**: Daily, monthly, and aggregated enrollment numbers
- **Time Period**: Temporal data with date information
- **Granularity**: National, State, and District level data
- **Files**: Split into 3 parts (`DF_ENROLMENT_1.csv` through `DF_ENROLMENT_3.csv`)

### Cleaned Datasets
- `DF_BIOMETRIC_CLEANED.csv` - Consolidated and cleaned biometric data
- `DF_DEMOGRAPHIC_CLEANED.csv` - Consolidated and cleaned demographic data
- `DF_ENROLMENT_CLEANED.csv` - Consolidated and cleaned enrolment data

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd c:\addhar
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r Adhaar_2026/streamlit_app_demo/requirements.txt
   ```

   Key dependencies include:
   - `streamlit` - Web app framework
   - `pandas` - Data manipulation
   - `matplotlib` & `seaborn` - Data visualization
   - `numpy` - Numerical computing

## 📈 Running the Streamlit Applications

The project includes three interactive Streamlit dashboards:

### 1. **Biometric Analytics Dashboard**
```bash
streamlit run Adhaar_2026/streamlit_app_demo/app_biometric.py
```
- Explore biometric enrollment patterns
- View age-wise distribution
- Analyze state-wise and district-wise biometric data
- Interactive visualizations and statistics

### 2. **Demographic Analytics Dashboard**
```bash
streamlit run Adhaar_2026/streamlit_app_demo/app_demographic.py
```
- Analyze demographic distribution of enrollees
- Explore age groups and gender distribution
- View state and district-level demographic insights
- Population-based analysis

### 3. **Enrolment Analytics Dashboard**
```bash
streamlit run Adhaar_2026/streamlit_app_demo/app_enrolment.py
```
- Track enrollment trends over time
- Analyze monthly and temporal patterns
- Compare state and district performance
- Statistical anomaly detection

### 4. **Main Multi-Analytics App** (if available)
```bash
streamlit run Adhaar_2026/streamlit_app_demo/app2.py
```
- Combined view of all three datasets
- Cross-dataset analysis and insights

## 🔍 Dashboard Features

All dashboards include:
- **Multi-level Analysis**: National, State, and District levels
- **Interactive Filters**: Select specific states and districts
- **Data Visualizations**: Charts, graphs, and statistical plots
- **Indian Number Formatting**: Numbers displayed in Indian numbering system (e.g., 1,23,45,678)
- **Responsive Design**: Wide layout for better data visibility
- **Real-time Data Loading**: Efficient data caching with Streamlit

## 📁 Project Structure

```
addhar/
├── README.md                          # This file
├── split_csvs.ipynb                   # Notebook for splitting datasets
├── DF_BIOMETRIC_CLEANED.csv           # Consolidated biometric data
├── DF_DEMOGRAPHIC_CLEANED.csv         # Consolidated demographic data
├── DF_ENROLMENT_CLEANED.csv           # Consolidated enrolment data
├── Adhaar_2026/
│   ├── Datasets/
│   │   ├── DF_BIOMETRIC_1.csv to DF_BIOMETRIC_5.csv
│   │   ├── DF_DEMOGRAPHIC_1.csv to DF_DEMOGRAPHIC_5.csv
│   │   └── DF_ENROLMENT_1.csv to DF_ENROLMENT_3.csv
│   └── streamlit_app_demo/
│       ├── app_biometric.py           # Biometric dashboard
│       ├── app_demographic.py         # Demographic dashboard
│       ├── app_enrolment.py           # Enrolment dashboard
│       ├── app2.py                    # Combined dashboard
│       └── requirements.txt           # Python dependencies
└── Plots - images/                    # Generated visualizations and plots
```

## 💡 Usage Tips

1. **First Time Setup**: 
   - Install dependencies: `pip install -r requirements.txt`
   - Data files should be in `Adhaar_2026/Datasets/` directory

2. **Running Locally**:
   - Run `streamlit run <app_file>` in your terminal
   - Dashboard will open in your default browser at `http://localhost:8501`

3. **Data Filtering**:
   - Use sidebar controls to select analysis level (National/State/District)
   - Filter by state and district as needed
   - Visualizations update in real-time

4. **Performance**:
   - Data is cached after first load for faster interactions
   - Large datasets are split across multiple files for efficiency

## 📊 Data Format

The datasets contain:
- **Temporal Data**: Date-based enrolment information
- **Geographic Data**: State and district-level breakdown
- **Age Groups**: Multiple age brackets for demographic analysis
- **Counts**: Aggregated enrollment and biometric numbers

## 🛠️ Dependencies

Main packages used:
- `streamlit` - Interactive web dashboards
- `pandas` - Data processing and analysis
- `matplotlib` - Static visualizations
- `seaborn` - Statistical data visualization
- `numpy` - Numerical operations

See `Adhaar_2026/streamlit_app_demo/requirements.txt` for complete dependency list.

## 📝 Notes

- All numbers are formatted using Indian numbering system (Lakh, Crore system)
- Age groups vary between datasets for relevance to biometric/demographic analysis
- Data files are split to manage file sizes efficiently
- Dashboard themes and layouts are optimized for data exploration and reporting

## 🤝 Contributing

Feel free to improve visualizations, add new analysis features, or optimize data processing.

## 📧 Contact & Support

For issues or questions about the datasets or dashboards, please refer to the data documentation or contact the project maintainers.

---

**Last Updated**: January 2026
