# Olympics Data Analysis Project 🏅

## Overview
This project automates the extraction, transformation, and analysis of Olympics data using a combination of Python, SQL Server, and Tableau.

### Key Features
- **Automated Data Extraction**: A Python script that downloads the latest Olympics dataset from Kaggle, unzips it, and converts CSV files to Excel format.
- **Data Storage and Analysis**: The transformed data is stored in SQL Server, where crucial insights are derived using SQL queries.
- **Dynamic Dashboards**: The analyzed data is visualized through interactive Tableau dashboards. The user can filter based on the country and get important information about various statistics. 

## Data Source
The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/piterfm/paris-2024-olympic-summer-games), where it was updated daily during the course of Paris Olympics 2024.

## Project Structure
- `scripts/`: Contains the Python scripts for data extraction and transformation.
- `sql/`: SQL queries used for data analysis.
- `data/`: Contains the extracted and transformed data.
- `dashboards/`: Tableau dashboard images and related files.

## How It Works
1. **Data Extraction & Transformation**:
   - A Python script is scheduled via Windows Task Scheduler to run daily, ensuring the data is always up-to-date.
   - The script downloads the dataset, unzips it, converts CSV files to Excel, and stores them in a specified directory.

2. **Data Analysis**:
   - The Excel files are imported into SQL Server.
   - Various SQL queries are used to join relevant tables and extract meaningful insights from the data.
   - There are few queries that extract data relevant for Dashboard Development. 

3. **Data Visualization**:
   - The analyzed data is connected to Tableau, where dynamic dashboards are created to visualize key metrics and trends.
   - I have tried to gather as much insights possible as to athlete's age, demographics and likewise.

## Dashboards
Paris Olympics 2024 - Top 5 Countries

![Dashboard 1](Dashboards/Paris%202024%20Olympics%20Dashboard%20-%20Top%205%20Countries.png)

Paris Olympics 2024 - Overview

![Dashboard 2](Dashboards/Paris%202024%20Olympics%20Dashboard.png)

## How to Use
1. Clone this repository: `git clone <repository-url>`.
2. Set up the environment and install dependencies (Python, SQL Server, Tableau).
3. Update the Python script with your Kaggle API key.
4. Schedule the script using Windows Task Scheduler.
5. Open Tableau and connect to your SQL Server instance to view the dashboards.

## Acknowledgments
- Kaggle for providing the dataset.
- Python, SQL Server, and Tableau communities for their invaluable tools and resources.

