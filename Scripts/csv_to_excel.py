import os
import pandas as pd

# Define the directory containing your CSV files
csv_directory = 'C:\\Users\\Animesh\\OneDrive - University of Texas at Arlington\\Desktop\\Andy\\Tableau Dashboards\\Olympics 2024'  # Replace with your directory

# Create an output directory for the Excel files
excel_directory = os.path.join(csv_directory, 'excel_files')
os.makedirs(excel_directory, exist_ok=True)

# Loop through all files in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        # Define full file paths
        csv_file_path = os.path.join(csv_directory, filename)
        excel_file_path = os.path.join(excel_directory, filename.replace('.csv', '.xlsx'))
        
        # Read the CSV file
        df = pd.read_csv(csv_file_path)
        
        # Save it as an Excel file
        df.to_excel(excel_file_path, index=False)
        
        print(f"Converted {filename} to {os.path.basename(excel_file_path)}")

print(f"All CSV files have been converted to Excel workbooks in {excel_directory}.")
